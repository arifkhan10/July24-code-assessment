from rest_framework import serializers
from student.models import College
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=College
        fields=("name","admnno","rollno","college","parentname")
