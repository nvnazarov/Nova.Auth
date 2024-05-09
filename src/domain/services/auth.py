from .. import dtos
from .. import repos
from .. import errors
from .. import hasher
from .. import token
from .. import validators


class AuthService:
    def __init__(self,
                 user_repo: repos.UserRepo, 
                 hasher: hasher.Hasher,
                 at_context: token.AccessTokenContext,
                 rt_context: token.RefreshTokenContext):
        self.user_repo = user_repo
        self.hasher = hasher
        self.at_context = at_context
        self.rt_context = rt_context
    
    
    async def authorize(self, credentials: dtos.AuthIn) -> dtos.AuthOut:
        user = await self.user_repo.find_by_email(credentials.email)

        if not user:
            raise errors.NoUser
        
        if not user.email_verified:
            raise errors.EmailNotVerified
        
        if not self.hasher.verify(credentials.password, user.password_hash):
            raise errors.WrongPassword
        
        access_token = self.at_context.generate(user)
        refresh_token = self.rt_context.generate(user)
        
        # TODO: save refresh token in db
        
        return dtos.AuthOut(access_token, refresh_token)
    
    
    async def register(self, credentials: dtos.RegistrationIn) -> dtos.RegistrationOut:
        if not validators.validate_email(credentials.email):
            raise errors.BadEmail
        
        if not validators.validate_password(credentials.password):
            raise errors.BadPassword
        
        user = await self.user_repo.find_by_email(credentials.email)
        
        if user:
            raise errors.UserExists
        
        password_hash = self.hasher.hash(credentials.password)
        dto = dtos.UserAdd(credentials.email, password_hash)
        user = await self.user_repo.add(dto)
        
        access_token = self.at_context.generate(user)
        refresh_token = self.rt_context.generate(user)
        
        return dtos.RegistrationOut(access_token, refresh_token)
    
    
    async def refresh(self):
        raise NotImplementedError