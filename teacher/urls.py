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


    user (student)
    name=Luffy
    pass=luffy123
"""
from django.urls import path,include
from django.contrib import admin
from teacher import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path('teacherclick', views.teacherclick_view),
    path('teachersignup', views.teacher_signup_view,name="teachersignup"),
    path('teacherlogin', LoginView.as_view(template_name="teacher/teacherlogin.html"),name="teacherlogin"),
    path('teacher-dashboard',views.teacher_dashboard_view, name="teacher-dashboard"),
    path('teacher-exam',views.teacher_exam_view, name="teacher-exam"),
    path('teacher-add-exam',views.teacher_add_exam_view, name="teacher-add-exam"),
    path('teacher-add-question',views.teacher_add_question_view, name="teacher-add-question"),
    path('teacher-view-exam',views.teacher_view_exam_view, name="teacher-view-exam"),
    path('teacher-view-student',views.teacher_view_student_view, name="teacher-view-student"),
    path('teacher-question',views.teacher_question_view, name="teacher-question"),
    path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),
    path('teacher-delete-student/<int:pk>',views.teacher_delete_student_view, name="teacher-delete-student"),
    path('teacher-update-student/<int:pk>',views.teacher_update_student_view, name="teacher-update-student"),
    path('teacher-view-question',views.teacher_view_question_view, name="teacher-view-question"),
    path('see-question/<int:pk>',views.see_question_view, name="see-question"),
    path('remove-question/<int:pk>',views.remove_question_view, name="remove-question"),
    
    
    path('teacher-result',views.teacher_result_view, name="teacher-result"),
    path('teacher-check-course/<int:pk>',views.teacher_check_course_view, name="teacher-check-course"),
    path('teacher-view-result/<int:pk>',views.teacher_view_result_view, name="teacher-view-result"),
]