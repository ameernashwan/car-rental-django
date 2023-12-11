from typing import Optional, List

from ninja import Schema
from pydantic import EmailStr, Field

from realestate.schemas import HomeOut


class AccountCreate(Schema):
    full_name : str
    phone_number: Optional[str]
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str


class AccountOut(Schema):
    full_name : str = None
    email: EmailStr = None
    phone_number: str = None

class Profile(Schema):
    account: AccountOut = None
    realestates: List[HomeOut] = None


class TokenOut(Schema):
    access: str

class AuthOut(Schema):
    token: TokenOut
    account: AccountOut

class SigninSchema(Schema):
    email: EmailStr
    password: str


class AccountUpdate(Schema):
    full_name : str
    phone_number: Optional[str]


class ChangePasswordSchema(Schema):
    old_password: str
    new_password1: str
    new_password2: str

