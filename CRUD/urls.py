from django.urls import path
from .import views

urlpatterns=[
    path('',views.EmployeeCreate.as_view()),
    path('list/',views.Employeelist.as_view()),
    path('details/<pk>/',views.Employeedetail.as_view()),
    path('update/<pk>/',views.Employeeupdate.as_view()),
    path('delete/<pk>/',views.Employeedelete.as_view())
]