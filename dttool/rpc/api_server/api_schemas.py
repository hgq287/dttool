from pydantic import AwareDatetime, BaseModel, RootModel, SerializeAsAny, model_validator

class Ping(BaseModel):
  status: str

class Version(BaseModel):
  version: str