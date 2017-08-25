from django.shortcuts import render
from rest_framework import viewsets
from Backend.models import (
	Student
)
from Backend.serializers import StudentSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

# Create your views here.

class StudentControl(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	@list_route(methods=["get"],url_path="student_list")
	def get_student_data(self,request,*args,**kwargs):
		try:
			student = Student.objects.all().order_by('name')
			serializer = self.serializer_class(student, many=True)
			return Response(serializer.data)
		except Exception as e:
			return Response({"error":e})

	@detail_route(methods=["get"],url_path="student_view")
	def get_student(self,request,pk=None,*args,**kwargs):
		try:
			student = Student.objects.get(id=pk)
			serializer = self.serializer_class(student)
			return Response(serializer.data)
		except Student.DoesNotExist:
			return Response("No data")
		
	@detail_route(methods=["post"])
	def add_student(self,request,pk=None,*args,**kwargs):
		student = self.get_object()
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			student.save()
			return Response("Success")
		else:
			return Response("Not Valid Data")

	@detail_route(methods=["put"])
	def update_student(self,request,pk=None,*args,**kwargs):
		student = self.get_object()
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			student.update(id=pk)
			return Response("Success")
		else:
			return Response("Not Valid data")

	@detail_route(methods=["delete"])
	def delete_student(self,request,pk=None,*args,**kwargs):
		student = self.get_object(pk)
		try:
			student.delete()
			return Response("Success")
		except student.DoesNotExist:
			return Response("Failed")