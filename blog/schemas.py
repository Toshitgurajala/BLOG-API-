from pydantic import BaseModel
from typing import List,Optional

class blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode=True

class usershoe(BaseModel):
    name:str
    email:str
    blogs:List[blog]=[]
    class Config():
        orm_mode=True


class usershowonly(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class BlogBase(BaseModel):

    title:str
    body:str
    creator:usershowonly
    class Config():
        orm_mode=True


class user(BaseModel):
    name:str
    email:str
    password:str

class login(BaseModel):
    username:str
    password:str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
     email: Optional[str] = None
