from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class StudentSchema(BaseModel):
    id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    phone_number: Optional[int]=None
    password: Optional[str]=None
    
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