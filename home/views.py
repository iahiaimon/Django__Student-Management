from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

from .models import AddStudent
from .forms import AddStudentForm

# Create your views here.


def home(request):
    students = AddStudent.objects.all()
    return render(request, "home.html", {"students": students})


def addstudent(request):

    if not request.user.is_authenticated:
        messages.error(request, "You have to login first to add a new student")
        return redirect("home")

    form = AddStudentForm()

    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student added successfully! ")
            return redirect("home")
        else:
            messages.error(
                request, "❌ Failed to add student. Please check your input."
            )

    return render(request, "add_student.html", {"form": form})


@login_required
def studentdetails(request, id):

    if not request.user.is_authenticated:
        messages.error(request, "You have to login first to see student details.")
        return render(request, "home.html", {"students": AddStudent.objects.all()})
    student = AddStudent.objects.get(id=id)

    return render(request, "details.html", {"student": student})


@login_required
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
            messages.error(
                request, "❌ Failed to update student data. Please check your input."
            )

    return render(request, "add_student.html", {"form": form, "edit": True})


@login_required
def deletestudent(request, id):
    if request.user.is_superuser and request.user.username == "Iahia":
        try:
            student = AddStudent.objects.get(id=id)
            student.delete()
            messages.success(request, "✅ Student deleted successfully!")
        except AddStudent.DoesNotExist:
            messages.error(request, "❌ Student not found!")
    else:
        messages.error(request, "❌ You do not have permission to delete this item.")

    return redirect("home")


User = get_user_model()


def user_login(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

        user = User.objects.filter(username=name).first()

        if user is not None:
            # Authenticate the user
            authenticated_user = authenticate(
                request, username=user.username, password=password
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("home")
            else:
                messages.error(request, "Invalid password.")
        else:
            messages.error(request, "User not found.")

    return render(request, "login.html")
