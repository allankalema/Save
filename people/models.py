from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class CustomeUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        """
        This method is necessary for authentication with the username field.
        """
        return self.get(username=username)


class CustomeUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomeUserManager()  # Attach the custom manager to the model

    def __str__(self):
        return self.username



class UserActivity(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE, related_name='activity')
    posts = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    comments = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    likes = models.PositiveBigIntegerField(default=0, null=True, blank=True)

    def total_activity(self):
        return self.posts + self.comments + self.likes

    def __str__(self):
        return f"Activity for {self.user.username}"
