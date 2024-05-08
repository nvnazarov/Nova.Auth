class AuthError(Exception):
    pass


class NoUser(AuthError):
    pass


class UserExists(AuthError):
    pass


class WrongPassword(AuthError):
    pass


class BadPassword(AuthError):
    pass


class BadToken(AuthError):
    pass