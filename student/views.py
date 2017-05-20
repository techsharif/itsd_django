from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from student.models import Student


class StudentListView(View):
    def get(self,request):
        students = Student.objects.all()
        return render(request,'student/student_list.html',{'students':students})

