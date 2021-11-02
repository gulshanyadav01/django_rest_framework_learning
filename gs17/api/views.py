from re import T
from django.shortcuts import render 

from rest_framework.response import Response 
from .models import Student 
from .serializers import StudentSerializer
from rest_framework import status 
from rest_framework import viewsets

from gs17.api import serializers 


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)