import logging
import threading
from contextvars import ContextVar
from typing import Any, Final, Optional

from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import NoSuchModuleError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from dttool.exceptions import OperationalException

logger = logging.getLogger(__name__)

_SQL_DOCS_URL = "http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls"

def init_db(db_url: str) -> None:
  """
  Initializes this module with the given config,
  registers all known command handlers
  and starts polling for message updates
  :param db_url: Database to use
  :return: None
  """

  kwargs: dict[str, Any] = {} 

  if db_url == "sqlite:///":
    raise OperationalException(
      f"Bad db-url {db_url}. For in-memory database, please use `sqlite://`."
    )
  if db_url == "sqlite://":
    kwargs.update(
        {
            "poolclass": StaticPool,
        }
    )
    # Take care of thread ownership
    if db_url.startswith("sqlite://"):
      kwargs.update(
          {
              "connect_args": {"check_same_thread": False},
          }
      )

    try:
      engine = create_engine(db_url, future=True, **kwargs)
    except NoSuchModuleError:
      raise OperationalException(
          f"Given value for db_url: '{db_url}' "
          f"is no valid database URL! (See {_SQL_DOCS_URL})"
      )