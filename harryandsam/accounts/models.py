from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, number, address, city, sprc, postal, waiver, password=None,):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not number:
            raise ValueError("Users must have a phone number, Mobile number preffered")
        if not address:
            raise ValueError("Users must have an address")
        if not city:
            raise ValueError("Users must enter their city")
        if not sprc:
            raise ValueError("Please enter your state, province, region or city")
        if not postal:
            raise ValueError("Users must have a postal code")
        if not waiver:
            raise ValueError("Users must agree to the policies and waivers")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            number=number,
            address=address,
            sprc=sprc,
            city=city,
            postal=postal,
            waiver=waiver,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password, first_name, last_name, number, address, city, sprc, postal, waiver):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            number=number,
            address=address,
            sprc=sprc,
            city=city,
            postal=postal,
            waiver=waiver,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Accounts(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=40, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    number = PhoneNumberField(verbose_name='Phone Number', null=False, blank=False, unique=False)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    sprc = models.CharField(verbose_name='Address 2', max_length=120)
    postal = models.CharField(max_length=10)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    waiver = models.BooleanField(verbose_name='I agree', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','number','address','sprc','city','postal','waiver']

    objects = MyAccountManager()

    class Meta:
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.first_name + " " + self.last_name + "(" + self.username + ")"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True