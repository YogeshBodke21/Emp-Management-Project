from django.urls import path
from .views import employeeView, add_emp, delete_view, show_view, filter_view

urlpatterns = [
    path('emp/', employeeView, name="emp"),
    path("add/", add_emp, name= "add"),
    path("show/",show_view, name= "show"),
    path("delete/<int:pk>/", delete_view, name= "delete"),
    path("filter/", filter_view, name= "filter"),
    path('fil/', filter_view, name="fil"),

]
