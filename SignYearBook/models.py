from django.db import models
from user.models import CustomUser
# Create your models here.


class YearbookSignature(models.Model):
    StudentProfile = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,related_name='NameOfStudentProfile')
    StudentSigning = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,related_name='NameOfStudent')
    Comment = models.CharField(max_length=255,blank=True)
    DateAdded = models.DateTimeField(null=True)
    def __str__(self):
        "17cg0093493 signed 17hfd899000 profile"
        return str(self.StudentProfile.Matno) +'Signed '+ str(self.StudentSigning.Matno) +'Profile'