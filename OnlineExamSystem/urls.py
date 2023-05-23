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
"""
from django.urls import path,include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),

    path('',views.home_view,name=''),
    path('contactus', views.contactus_view),
    path('adminclick', views.adminclick_view),
    path('adminlogin',LoginView.as_view(template_name = "exam/adminlogin.html"),name='adminlogin'),
    path('logout',LogoutView.as_view(template_name='exam/logout.html'),name='logout'),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('admin-dashboard',views.admin_dashboard_view,name='admin-dashboard'),

    # Admin teacher related Urls 
    path('admin-teacher',views.admin_teacher_view,name='admin-teacher'),
    path('admin-view-teacher',views.admin_view_teacher_view,name='admin-view-teacher'),
    path('update-teacher/<int:pk>',views.update_teacher_view,name='update-teacher'),
    path('delete-teacher/<int:pk>',views.delete_teacher_view,name='delete-teacher'),
    path('admin-view-pending-teacher',views.admin_view_pending_teacher_view,name='admin-view-pending-teacher'),
    path('approve-teacher/<int:pk>',views.approve_teacher_view,name='approve-teacher'),
    path('reject-teacher/<int:pk>',views.approve_teacher_view,name='reject-teacher'),


    # Admin Student Section Urls 
    path('admin-student',views.admin_student_view,name='admin-student'),
    path('admin-view-student',views.admin_view_student_view,name='admin-view-student'),
    path('admin-view-student-marks', views.admin_view_student_marks_view,name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    
    # Admin Course related Urls 
    path('admin-course',views.admin_course_view,name = 'admin-course'),
    path('admin-add-course',views.admin_add_course_view,name = 'admin-add-course'),
    path('admin-view-course',views.admin_view_course_view,name = 'admin-view-course'),
    path('delete-course/<int:pk>',views.delete_course_view,name='delete-course'),

    # Admin Question related Urls 
    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>',views.view_question_view,name='view-question'),
    path('delete-question/<int:pk>',views.delete_question_view,name='delete-question'),


]

