from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class MyUserManager(BaseUserManager):

    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User Must have Email")
        else:
            user = self.model(
             email = self.normalize_email(email),
            )
            user.set_password(password)
            user.save(using=self._db)
            return user
    def create_superuser(self,email,password):
        if not email:
            raise ValueError("User Must have Email")
        else:
            user = self.model(
             email = self.normalize_email(email),
             is_admin =True,
             is_staff = True
            )
            user.set_password(password)

            user.save(using=self._db)
            return user



class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_lab = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_medical = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=10,blank=True,null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
