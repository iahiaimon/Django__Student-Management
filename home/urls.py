from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name = 'home'),
    path('addstudent/' , views.addstudent , name = "addstudent"),
    path('studentdetails/<int:id>/' , views.studentdetails , name = "studentdetails"),
    path('editstudent/<int:id>/' , views.editstudent , name = "editstudent"),
    path('deletestudent/<int:id>/' , views.deletestudent , name = "deletestudent"),
    path('login/' , views.user_login , name = "login"),
]