from django import forms
from . import models


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = models.AddStudent
        fields = ["name", "email", "phone", "address", "course", "image"]
