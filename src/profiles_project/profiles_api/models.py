from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Helps Django to work on our custom model'''

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, name, password):
        '''Creates and saves a super user with given details'''

        super_user = self.create_user(email, name, password)
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save(using=self._db)

        return super_user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''
    Represents a user profile inside our system.
    '''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ''' Returns full name of the user'''
        return self.name

    def get_short_name(self):
        '''Returns short name of the user'''
        return self.name

    def __str__(self):
        '''Returns email for the objects created'''
        return self.email
