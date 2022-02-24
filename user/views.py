from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,permission_required
import pandas as pd
from user.models import CustomUser,College,Department,Program
from django.contrib.auth.hashers import make_password
# Create your views here.

@login_required(login_url='/Account/log_in/')
@permission_required('is_superuser', 'forbidden')
def UploadUser(request):
    if request.POST:
        if request.FILES['UploadName']:
            df = pd.read_csv (request.FILES['UploadName'])
            for i in range(0,len(df)):
                if str(df.iloc[i].regno) :
                    college = College.objects.create(NameOfCollege=df.iloc[i].college,Image='college/'+str(df.iloc[i].college)+'.jpg') if not  College.objects.filter(NameOfCollege=df.iloc[i].college) else  College.objects.get(NameOfCollege=df.iloc[i].college)
                    dept = Department.objects.create(NameOfCollege=college,NameOfDepartment=df.iloc[i].dept,Image='department/'+str(df.iloc[i].dept)+'.jpg') if not Department.objects.filter(
                        NameOfDepartment=df.iloc[i].dept) else Department.objects.get(NameOfCollege=college,NameOfDepartment=df.iloc[i].dept)
                    program = Program.objects.create(NameOfCollege=college,
                                                     NameOfDepartment=dept,
                                                     NameOfProgram=df.iloc[i].program,Image='program/'+str(df.iloc[i].program)+'.jpg') if not Program.objects.filter(
                        NameOfProgram=df.iloc[i].program) else Program.objects.get(NameOfCollege=college,
                                                                                      NameOfDepartment=dept, NameOfProgram=df.iloc[i].program)
                    fullname = str(df.iloc[i].fullname).split(' ')

                    email = fullname[1]+'.'+fullname[0]+'@stu.cu.edu.ng'
                    if not (CustomUser.objects.filter(Matno=df.iloc[i].matricno) and CustomUser.objects.filter(Regno=df.iloc[i].regno,)and CustomUser.objects.filter(email=email)):
                        CustomUser.objects.create(Matno=df.iloc[i].matricno,
                                                                    ProfilePic='student/'+str(df.iloc[i].matricno)+'.JPG',password=make_password(str(df.iloc[i].regno))
                                                  ,email=email,FirstName=fullname[0],MiddleName=fullname[2],
                                                  LastName=fullname[1],Regno=df.iloc[i].regno,college=college,program=program,department=dept)
                    elif CustomUser.objects.filter(email=email):
                        CustomUser.objects.filter(email=email).update(Matno=df.iloc[i].matricno,
                                                                      email=email,FirstName=fullname[0],
                                                                      MiddleName=fullname[2],LastName=fullname[1],
                                                                    ProfilePic='student/'+str(df.iloc[i].matricno)+'.JPG',
                                                                      Regno=df.iloc[i].regno,college=college,program=program,department=dept)
                    elif  CustomUser.objects.filter(Matno=df.iloc[i].matricno):
                        CustomUser.objects.filter(Matno=df.iloc[i].matricno).update(Matno=df.iloc[i].matricno,email=email,FirstName=fullname[0],
                                                                      MiddleName=fullname[2],LastName=fullname[1],
                                                                    ProfilePic='student/'+str(df.iloc[i].matricno)+'.JPG',
                                                                      Regno=df.iloc[i].regno,college=college,program=program,department=dept)
                    # if CustomUser.objects.get(Matno=df.iloc[i].matricno).email=='Adegbola.Babs-Ogunleye@stu.cu.edu.ng':
                    #
                    #     pass
                    # else:
                    #     CustomUser.objects.get(Matno=df.iloc[i].matricno).delete()


            #
            # Program.objects.all().delete()
            # Department.objects.all().delete()
            # College.objects.all().delete()

    return render(request,'AccountCreation.html',context={})