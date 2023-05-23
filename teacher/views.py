from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import models,forms
from django.db.models import Sum
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group
from student import models as SMODEL
from student import forms as SFORM
from exam import models as QMODEL
from exam import forms as QFORM
from django.conf import settings
from datetime import date, timedelta

# Create your views here.


def teacherclick_view(request):
    return render(request,'teacher/teacherclick.html')

def teacher_signup_view(request):
    userForm = forms.TeacherUserForm()
    teacherForm = forms.TeacherForm()
    mydict = {
        'userForm':userForm, 'teacherForm':teacherForm
    }
    if request.method == 'POST':
        userForm = forms.TeacherUserForm(request.POST)
        teacherForm = forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            teacher = teacherForm.save(commit=False)
            teacher.user = user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    return render(request,'teacher/teachersignup.html',context=mydict)


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    dict = {
        'students' : SMODEL.Student.objects.all().count(),
        'courses' : QMODEL.Course.objects.all().count(),
        'questions' : QMODEL.Question.objects.all().count()
    }

    return render(request,'teacher/teacher_dashboard.html',context=dict)



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_exam_view(request):
    return render(request,'teacher/teacher_exam.html')




@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_exam_view(request):
    courseForm = QFORM.CourseForm()
    if request.method == "POST":
        courseForm = QFORM.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print('Form is invalid')
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request,'teacher/teacher_add_exam.html',{'courseForm':courseForm})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_exam.html',{'courses':courses})



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_question_view(request):
    return render(request,'teacher/teacher_question.html')



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_question.html',{'courses':courses})





@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_question_view(request,pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_question.html',{'questions':questions})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request,'teacher/teacher_add_question.html',{'questionForm':questionForm})



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_question_view(request,pk):
    question= QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')


#Student section

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_student_view(request):
    students = SMODEL.Student.objects.all()
    return render(request,'teacher/teacher_view_student.html',{'students':students})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_update_student_view(request,pk):
    student=SMODEL.Student.objects.get(id=pk)
    user=SMODEL.User.objects.get(id=student.user_id)
    userForm=SFORM.StudentUserForm(instance=user)
    studentForm=SFORM.StudentForm(request.FILES,instance=student)
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=SFORM.StudentUserForm(request.POST,instance=user)
        studentForm=SFORM.StudentForm(request.POST,request.FILES,instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect('teacher-view-student')
    return render(request,'teacher/teacher_update_student.html',context=mydict)


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_delete_student_view(request,pk):
    student = SMODEL.Student.objects.get(id=pk)
    user = SMODEL.User.objects.get(id = student.user_id)
    user.delete()
    student.delete()
    return HttpResponseRedirect('/teacher-view-student')





@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_result_view(request):
    students = SMODEL.Student.objects.all()
    return render(request,'teacher/teacher_result.html',{'students':students})



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_check_course_view(request,pk):
    courses = QMODEL.Course.objects.all()
    response = render(request,'teacher/teacher_check_course.html',{'courses':courses})
    response.set_cookie('student_id',str(pk))
    return response



@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_result_view(request,pk):
    course = QMODEL.Course.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student = SMODEL.Student.objects.get(id=student_id)
    results = QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'teacher/teacher_view_results.html',{'results':results})