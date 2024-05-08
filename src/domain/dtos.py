from dataclasses import dataclass


@dataclass
class RegistrationIn:
    email: str
    password: str


@dataclass
class RegistrationOut:
    access_token: str
    refresh_token: str


@dataclass
class AuthIn:
    email: str
    password: str


@dataclass
class AuthOut:
    access_token: str
    refresh_token: str


@dataclass
class UserAdd:
    email: str
    password_hash: str