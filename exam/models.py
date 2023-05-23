from django.db import models
from student.models import Student
# Create your models here.

# we have not donw admin.site.register for these models
# so they will not be dispalyed in admin of project

class Course(models.Model):
     
    course_name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=50)
    question_numbers = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()


    # class Meta:
    #     verbose_name = _("Course")
    #     verbose_name_plural = _("Courses")

    def __str__(self):
        return self.course_name
    
    @property
    def get_instance(self):
        return self


class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)



class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    
