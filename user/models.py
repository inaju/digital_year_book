from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager
from django.core.files.storage import FileSystemStorage


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]

college_storage = 'college'
department_storage = 'department'
program_storage = 'program'
student_storage = 'student'


class College(models.Model):
    NameOfCollege = models.CharField(max_length=255)
    Image = models.ImageField(upload_to=college_storage)
    # Image = models.ImageField()

    def __str__(self):
        return str(self.NameOfCollege)


class Department(models.Model):
    NameOfCollege = models.ForeignKey(College, on_delete=models.DO_NOTHING)
    NameOfDepartment = models.CharField(max_length=255)
    Image = models.ImageField(upload_to=department_storage)
    # Image = models.ImageField()

    def __str__(self):
        return str(self.NameOfDepartment)


class Program(models.Model):
    NameOfProgram = models.CharField(max_length=255)
    NameOfCollege = models.ForeignKey(College, on_delete=models.DO_NOTHING)
    NameOfDepartment = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING)
    # Image = models.ImageField()
    Image = models.ImageField(upload_to=program_storage)

    def __str__(self):
        return str(self.NameOfProgram)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('student email address'), unique=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255)

    Regno = models.CharField(max_length=255,null=True)
    Matno = models.CharField(max_length=255,)
    OtherEmail = models.CharField(max_length=255, )
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    DOB = models.DateField(null=True)
    ProfilePic = models.ImageField(upload_to=student_storage)
    BIO = models.TextField(max_length=255)
    IGhandle = models.CharField(max_length=255)
    Twitter = models.CharField(max_length=255)
    linkedln = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
