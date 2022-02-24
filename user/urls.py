
from django.urls import path, include
from user import views

urlpatterns = [
    path('upload',views.UploadUser ,name='UploadUser'),
]