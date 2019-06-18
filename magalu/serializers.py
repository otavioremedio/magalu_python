from rest_framework import serializers
from .models import Employee
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Department
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:

        model = Employee
        fields = ('name','email','department')