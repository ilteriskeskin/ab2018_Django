from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The given username must be set')

        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None):
        return self._create_user(email, password, False, False)

    def create_superuser(self, email=None, password=None):
        return self._create_user(email, password, True, True)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('İsim', max_length=100)
    email = models.EmailField('E-Posta', max_length=100, unique=True)
    is_active = models.BooleanField("E-posta Onayı?", null=False, blank=False, default=False)
    is_staff = models.BooleanField("Staff?", null=False, blank=False, default=False)
    is_superuser = models.BooleanField("Superuser?", null=False, blank=False, default=False)
    created_at = models.DateTimeField('Kayıt Tarihi', auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = UserProfileManager()

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name