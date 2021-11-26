from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


from books.models import BookInfo, RentInfo
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, real_name, password=None):
        if not email:
            raise ValueError('이메일은 필수입니다')
        user = self.model(
            email=self.normalize_email(email),
            real_name=real_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, real_name, password):
        user = self.create_user(
            email,
            password=password,
            real_name=real_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    real_name = models.CharField(max_length=100)

    #유저 모델의 필수 필드
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()# 헬퍼 클래스를 사용하도록 설정

    USERNAME_FIELD = 'email'# username 필드를 email로 사용하도록 설정
    REQUIRED_FIELDS = ['real_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):#True를 반환하여 권한이 있음을 알림
        return True

    def has_module_perms(self, app_label):#True를 반환하여 주어진 앱(App)의 모델(Model)에 접근 가능
        return True

    @property
    def is_staff(self):#True가 반환되면 장고(django)의 관리자 화면에 로그인
        return self.is_admin

    def get_rent_books(self):
        return BookInfo.objects.filter(rent_info__user=self)

    def get_rent_history(self):
        return RentInfo.objects.filter(user=self)