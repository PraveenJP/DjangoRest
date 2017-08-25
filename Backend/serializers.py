from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializer(ModelSerializer):
	class Meta:
		model = Student
		fields = ["name","age","home_group","stud_class","father_name"]