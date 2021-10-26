from rest_framework import serializers
from .models import Student 

#validators 

class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("name should start with r")

    name = serializers.Charfield(validators = [start_with_r])
    
    class Meta:
        model  = Student
        fields = ['name','roll','city']
    
    
    # field level validation 
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("seat full")
        return value

    # object level validation : when we need to do validation that re
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'gulshan' and ct.lower() != 'noida':
            raise serializers.ValidationError("city must be noida")
        return data 
         
