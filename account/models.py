import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager

from config.utils.models import BaseEntity


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, full_name, email, password=None):
        if not email:
            raise ValueError("user must have email")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.full_name = full_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError("user must have email")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, BaseEntity):
    username = models.NOT_PROVIDED
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=255, null=False)
    language = models.CharField(max_length=255, null=False)
    is_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name="account_users")
    user_permissions = models.ManyToManyField(
        Permission, related_name="account_users_permissions"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
