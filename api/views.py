from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from user.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from SignYearBook.models import YearbookSignature
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def show_program_detail(request, program, format=None):
    """
    Return a list of all users.
    """
    print(program)
    program = [program for program in CustomUser.objects.filter(
        program__NameOfProgram=str(program))]
    serializer = CustomUserDetailsSerializer(program, many=True)
    return JsonResponse(serializer.data, safe=False)
    # return Response(program)



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def showstudentdetail(request, student, format=None):

    print(student)
    student_user = [student for student in CustomUser.objects.filter(
        Matno=str(student))]
    print(student_user)

    serializer = CustomUserDetailsSerializer(student_user, many=True)
    return JsonResponse(serializer.data, safe=False)
    # return Response(program)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def show_department_detail(request, department, format=None):

    print(department)
    department = [department for department in Program.objects.filter(
        NameOfDepartment__NameOfDepartment=str(department))]
    print(department)
    serializer = ShowProgramSerializer(department, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def show_college_detail(request, college, format=None):
    """
    Return a list of all users.
    """

    college_detail = [college for college in College.objects.filter(
        NameOfCollege=str(college))]

    college_detail_id = [college.id for college in College.objects.filter(
        NameOfCollege=str(college))][0]

    department_in_college_detail = [department for department in Department.objects.filter(
        NameOfCollege=str(college_detail_id))]

    # print(department_in_college_detail[0][1])

    serializer_college_detail = ShowCollegeSerializer(
        college_detail, many=True)

    serializer_department_in_college_detail = ShowDepartmentInCollegeSerializer(
        department_in_college_detail, many=True)
    response = {
        'college': serializer_college_detail.data,
        'department': serializer_department_in_college_detail.data
    }

    return JsonResponse(response, safe=False)



@api_view(['GET'])
def ShowCollege(request,format=None):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = College.objects.all()
        serializer = ShowCollegeSerializer(
            queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def ShowSignature(request, format=None):
    print(request.user)
    # print(department)
    Signed = [Signed for Signed in YearbookSignature.objects.filter(
        StudentProfile__email= str(request.user))]
    #
    # serializer = ShowDepartmentSerializer(department, many=True)
    user = [{'user':str(request.user)}]
    serializer = YearbookSignatureSerializer(
        Signed, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def PostSignature(request, format=None, ):
    studentProfile = str(request.data['Email'])
    user = str(request.user)
    if ( CustomUser.objects.filter(email=studentProfile,) and CustomUser.objects.filter(email=user) ):
        if not YearbookSignature.objects.filter(StudentProfile__email=studentProfile,StudentSigning__email=user):
            studentProfile = CustomUser.objects.get(email=studentProfile)
            user = CustomUser.objects.get(email=str(request.user))
            singed = YearbookSignature.objects.create(StudentProfile=studentProfile, StudentSigning=user,DateAdded=date.today(),Comment=request.data['Comment'])
        else:
            return HttpResponse('You have a record already')
    else:
        return HttpResponse('Check detail')
    #
    # serializer = ShowDepartmentSerializer(department, many=True)
    user = [{'user': str(request.user)}]


    return HttpResponse('Saved')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def UpdateSignature(request,pk, format=None, ):
    studentProfile = str(request.data['Email'])
    user = str(request.user)
    if ( CustomUser.objects.filter(email=studentProfile,) and CustomUser.objects.filter(email=user) ):
        studentProfile = CustomUser.objects.get(email=studentProfile)
        user = CustomUser.objects.get(email=str(request.user))
        if YearbookSignature.objects.filter(id=pk):
            if YearbookSignature.objects.get(id=pk).StudentSigning==user:
                singed = YearbookSignature.objects.filter(id=pk).update(StudentProfile=studentProfile,DateAdded=date.today(), StudentSigning=user,Comment=request.data['Comment'])
            else:
                return HttpResponse('you can\'t edit this record')
        else:
            return HttpResponse('This record does not exist')
    else:
        return HttpResponse('Check detail')
    #
    # serializer = ShowDepartmentSerializer(department, many=True)
    user = [{'user': str(request.user)}]


    return HttpResponse('Saved')

@api_view(['DElETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def DeleteSignature(request,pk, format=None, ):
    studentProfile = str(request.data['Email'])
    user = str(request.user)
    if ( CustomUser.objects.filter(email=studentProfile,) and CustomUser.objects.filter(email=user) ):
        studentProfile = CustomUser.objects.get(email=studentProfile)
        user = CustomUser.objects.get(email=str(request.user))

        if YearbookSignature.objects.filter(id=pk):
            if YearbookSignature.objects.get(id=pk).StudentSigning==user:
                singed = YearbookSignature.objects.get(id=pk, StudentProfile=studentProfile, StudentSigning=user, ).delete()
            else:
                return HttpResponse('you can\'t edit this record')
        else:
            return HttpResponse('This record does not exist')
    else:
        return HttpResponse('Check detail')
    #
    # serializer = ShowDepartmentSerializer(department, many=True)
    user = [{'user': str(request.user)}]


    return HttpResponse('Saved')
