from .models import Complaint_Details,Outpass_Details
from rest_framework import serializers
class OutpassSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Complaint_Details
        fields='__all__'
class ComplaintSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Outpass_Details
        fields='__all__'