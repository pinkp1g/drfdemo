from rest_framework import serializers
# 序列化基类
# serializers.Serializers
# serializers.ModelSerializer
from .models import Student
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

