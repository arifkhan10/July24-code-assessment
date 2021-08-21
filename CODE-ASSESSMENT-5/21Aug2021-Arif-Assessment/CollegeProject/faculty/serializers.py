from rest_framework import serializers
from faculty.models import Faculty
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=("fcode","name","department","address","mobilenumber","username","password")