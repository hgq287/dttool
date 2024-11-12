class DttoolException(Exception):
  """
  Dttool base exception. Handled at the outermost level.
  All other exception types are subclasses of this exception type.
  """


class OperationalException(DttoolException):
  """
  Requires manual intervention and will stop the bot.
  Most of the time, this is caused by an invalid Configuration.
  """


class ConfigurationError(OperationalException):
  """
  Configuration error. Usually caused by invalid configuration.
  """