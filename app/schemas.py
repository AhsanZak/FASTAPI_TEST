from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class StudentSchema(BaseModel):
    id: Optional[int]=None
    full_name: str
    email: str
    phone_number: int
    password: str
    profile_image: str

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]