from uuid import UUID
from dataclasses import dataclass


@dataclass
class User:
    user_id: UUID
    email: str
    password_hash: str
    email_verified: bool