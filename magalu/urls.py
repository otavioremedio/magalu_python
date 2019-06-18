from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^employee/$', views.EmployeeList.as_view(), name='employee-list'),
]