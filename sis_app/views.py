from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import datetime
from django.http import JsonResponse
from .models import *
from .forms import *
from .filters import *



# def hello_world(request):
#     return render(request, 'sis_app/hello_world.html')
    

def StudentList(request):
    students = Student.objects.all()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs


    context = {'studentList' : students, 'myFilter': myFilter}
    return render(request,"sis_app/Student_List.html", context)

def studentForm(request,id=0):
    model = Student
    form_class = StudentForm
    if request.method == "GET":
        if id == 0: 
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request,"sis_app/Student_Form.html",{'form':form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/studentList')

# Create your views here.
