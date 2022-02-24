from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from . import views
urlpatterns = [
    path('user/', include('rest_auth.urls')),
    path('user/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),

    path('showprogramdetail/<str:program>/',
         views.show_program_detail, name="show_program_detail"),
    path('showstudentdetail/<str:student>/',
         views.showstudentdetail, name="showstudentdetail"),

    path('showdepartmentdetail/<str:department>',
         views.show_department_detail, name="show_department_detail"),

    path('showcollegedetail/<str:college>/',
         views.show_college_detail, name="show_college_detail"),
    path('showcollege/',
         views.ShowCollege, name="show_college"),
    path('ShowSignature',
         views.ShowSignature, name="ShowSignature"),
    path('PostSignature',
         views.PostSignature, name="PostSignature"),
    path('UpdateSignature/<str:pk>',
         views.UpdateSignature, name="UpdateSignature"),
    path('DeleteSignature/<str:pk>',
         views.DeleteSignature, name="DeleteSignature"),


    # path('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
    #      confirm_email, name='account_confirm_email'),

]
