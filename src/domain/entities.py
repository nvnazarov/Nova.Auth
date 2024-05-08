from uuid import UUID


class User:
    user_id: UUID
    email: str
    password_hash: str