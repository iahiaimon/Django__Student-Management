from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from .models import AddStudent
from .forms import AddStudentForm

# Create your views here.


def home(request):
    students = AddStudent.objects.all()
    return render(request, "home.html", {"students": students})


def addstudent(request):
    form = AddStudentForm()

    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student added successfully! ") 
            return redirect("home")
        else:
            messages.error(request, "❌ Failed to add student. Please check your input.")

    return render(request, "add_student.html", {"form": form})



def studentdetails(request, id):
    student = AddStudent.objects.get(id=id)

    return render(request, "details.html", {"student": student})


def editstudent(request, id):
    student = AddStudent.objects.get(id=id)
    form = AddStudentForm(instance=student)
    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student data updated successfully! ") 
            return redirect("studentdetails", id=student.id)
        else:
            messages.error(request, "❌ Failed to update student data. Please check your input.")

    return render(request, "add_student.html", {"form": form, "edit": True})


def deletestudent(request, id):
    student = AddStudent.objects.get(id=id)
    student.delete()
    messages.success(request , "✅ Student deleted successfully! ")
    return redirect("home")
