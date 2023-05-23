"""
URL configuration for OnlineExamSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""super user
    username:samson
    pass:samson


    user 
    name=Luffy
    pass=luffy123
"""
from django.urls import path,include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
   
    path('studentclick',views.studentclick_view),
    path('studentlogin',LoginView.as_view(template_name="student/studentlogin.html"),name='studentlogin'),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('student-dashboard',views.student_dashboard_view,name='student-dashboard'),
    path('student-exam', views.student_exam_view,name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
    
    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
    path('view-result', views.view_result_view,name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('student-marks', views.student_marks_view,name='student-marks'),

]