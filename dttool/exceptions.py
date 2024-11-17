class DttoolException(Exception):
  """
  All other exception types are subclasses of this exception type.
  """


class OperationalException(DttoolException):
  """
  Most of the time, this is caused by an invalid Configuration.
  """


class ConfigurationError(OperationalException):
  """
  Configuration error. Usually caused by invalid configuration.
  """