from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from user.models import CustomUser, Program, Department, College
from SignYearBook.models import YearbookSignature
from user.models import GENDER_SELECTION
from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer, ReadOnlyField

class CustomRegisterSerializer(RegisterSerializer):
    # Matno = serializers.CharField(max_length=255)
    username = None
    email = serializers.CharField(max_length=255)
    FirstName = serializers.CharField(max_length=255)
    LastName = serializers.CharField(max_length=255)
    MiddleName = serializers.CharField(max_length=255)
    Matno = serializers.CharField(max_length=255)
    NameOfProgram = serializers.CharField(max_length=255)
    NameOfCollage = serializers.CharField(max_length=255)
    NameOfDepartment = serializers.CharField(max_length=255)

    # Define transaction.atomic to rollback the save operation in case of error

    @transaction.atomic
    def save(self, request):
        print()
        print()
        print()
        print()
        print()
        print(request.data['password1'])
        print()
        print()
        print()
        user = super().save(request)
        user.email = self.data.get('email')
        user.FirstName = self.data.get('FirstName')
        user.LastName = self.data.get('LastName')
        user.MiddleName = self.data.get('MiddleName')
        user.Matno = self.data.get('Matno')
        user.NameOfProgram = self.data.get('NameOfProgram')
        user.NameOfCollage = self.data.get('NameOfCollage')
        user.NameOfDepartment = self.data.get('NameOfDepartment')
        print()
        print()
        print()
        print()
        print()
        # if str(request.data['password1']) == str(request.data['password1']):
        #     raise ValueError(_("password1 and password2 are not the same"))
        user.set_password(str(request.data['password1']))
        user.save()
        return user


class ShowProgramSerializer(serializers.ModelSerializer):
    NameOfCollege = ReadOnlyField(source='NameOfCollege.NameOfCollege')
    NameOfDepartment = ReadOnlyField(source='NameOfDepartment.NameOfDepartment')
    class Meta:
        model = Program
        fields = ['NameOfProgram', 'NameOfCollege',
                  'NameOfDepartment', 'Image']


class ShowDepartmentSerializer(serializers.ModelSerializer):
    NameOfCollege = ReadOnlyField(source='NameOfCollege.NameOfCollege')
    class Meta:
        model = Department
        fields = ['NameOfCollege',
                  'NameOfDepartment', 'Image']


class ShowDepartmentInCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['NameOfDepartment', 'Image']


class ShowCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['NameOfCollege', 'Image']

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    college = ShowCollegeSerializer()
    department =ShowDepartmentInCollegeSerializer()
    program = ShowProgramSerializer()
    class Meta:
        model = CustomUser
        fields = (
            'FirstName',
            'LastName',
            'ProfilePic',
            'MiddleName',
            'Matno',
            'OtherEmail',
            'email',
            'gender',
            'DOB',
            'email',
            'IGhandle',
            'Twitter',
            'linkedln',
            'BIO',
            'college',
            'department',
            'program',
        )
        read_only_fields = ['email', 'phone_number',
                            'FirstName', 'LastName', 'MiddleName', 'Matno',]


class YearbookSignatureSerializer(serializers.ModelSerializer):
    StudentProfile = CustomUserDetailsSerializer()
    StudentSigning = CustomUserDetailsSerializer()
    class Meta:
        model = YearbookSignature
        fields = '__all__'
