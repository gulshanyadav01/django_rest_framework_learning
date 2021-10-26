from rest_framework import serializers
from .models import Student 

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['name']
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only': True}}


