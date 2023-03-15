

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname=None, username=None, profile_image=None, phonenumber=None, address=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname = nickname,
            username = username,
            profile_image = profile_image,
            phonenumber = phonenumber,
            address = address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname=None, username=None, profile_image=None, phonenumber=None, address=None, password=None):
        user = self.create_user(
            email,
            password=password,
            nickname = nickname,
            username = username,
            profile_image = profile_image,
            phonenumber = phonenumber,
            address = address,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True,)
    nickname = models.CharField(max_length=24, default=None, null=True, blank=True, unique=True)
    username = models.CharField(max_length=24, default=None, null=True, blank=True)
    profile_image = models.TextField(default=None, null=True, blank=True)
    phonenumber = models.IntegerField(default=None, null=True, unique=True, blank=True)
    address = models.TextField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.base_user import AbstractBaseUser


# class User(AbstractBaseUser):
#     """
#     이메일 = email
#     PW = password1
#     PW확인 = password2
#     닉네임 = nickname
#     이름 = username
#     프로필 이미지 = profile_image
#     전화번호 = phonenumber
#     주소 = address
#     """

#     email = models.EmailField()
#     nickname = models.CharField(max_length=24)
#     username = models.CharField(max_length=24)
#     profile_image = models.TextField()
#     phonenumber = models.CharField(max_length=24)
#     address = models.TextField()

#     class Meta:
#         db_table = "User"




# class User(AbstractBaseUser):
#     """
#     ID = userid
#     PW = password1
#     PW확인 = password2
#     닉네임 = nickname
#     이름 = username
#     전화번호 = phonenumber
#     주소 = address
#     """
#     email = models.EmailField(
#         verbose_name='email',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin






# class User(AbstractBaseUser):
#     # Default : id / password / last_login
#     # USER_TYPE_CHOICES = (
#     #     ('django', 'Django'),
#     #     ('django', 'Django'),
#     #     ('django', 'Django'),
#     # )
#     pass

# class UserManager(BaseUserManager):
#     def _create_user(self, email, username, password, gender = 1, **extra_fields):
#         if not email :
#             raise ValueError('The given email mist be set')
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         user = self.model(email = email, username = username, gender=gender, **extra_fields)
#         user.set_password(password)
#         user.save (using = self._db)
#         return user

#     def create_user(self, email, username = '', password = None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, username, password, **extra_fields)
    
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff = True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser = True')

#         return self._create_user(email, username, password, **extra_fields)

# GENDER_CHOICES = (
#     (0, 'Female'),
#     (1, 'Male'),
#     (2, 'Not to disclose')
# )

# class User(AbstractUser):
#     email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
#     username = models.CharField(max_length=30)
#     gender = models.SmallIntegerField(choices = GENDER_CHOICES)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return "<%d %s>" %(self.pk, self.email)



