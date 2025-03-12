from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



class AddStudent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=150)
    course = models.CharField(max_length=100)
    # course = models.ManyToManyField(Course)
    image = models.ImageField(upload_to="Images/", default="Images/student.png", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} -- {self.email}"


