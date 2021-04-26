from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return User

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_super', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    rank = [
        ('Supporter', 'Supporter (non-member)'),
        ('Anak', 'Anak'),
        ('Uso', 'Uso'),
        ('Chief', 'Chief'),
    ]

    tribe = [
        ('NaKoaHema', 'Na Koa Hema'),
        ('Alakai', 'Alaka\'i')
    ]

    username = models.CharField("user name", max_length=50, default='', unique=True)
    email = models.EmailField("email address", max_length=30, unique=True, blank=True)
    first_name = models.CharField("first name", max_length=50)
    last_name = models.CharField("last name", max_length=50)
    is_active = models.BooleanField('active', default=True)
    # password = models.CharField("password", unique=True, max_length=32, default='')
    id = models.AutoField(primary_key=True)
    is_staff = models.BooleanField('staff status', default=False)
    date_joined = models.DateField('date_joined', default=timezone.now)
    # ranking = models.CharField(choices=rank, max_length=50, default="Supporter")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']  # 'ranking'


    # Magic method returns string of self
    def __str__(self):
        return f"User {self.first_name} {self.last_name} rank {self.rank}".strip()

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class Anak(User):
    def __init__(self, tribe, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tribe = tribe.title()
        self.rank = User.rank[1]


class Uso(User):
    def __init__(self, first_name, last_name, tribe):
        super().__init__(first_name, last_name)
        self.tribe = tribe.title()
        self.rank = User.rank[2]