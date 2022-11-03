
from django import forms
from django.forms import ModelForm
from django import forms
from .models import Outpass_Details,Complaint_Details,Admin_Complaint_Details,Admin_Outpass_Details

class Outpass_detail_form(ModelForm):
    name=forms.TextInput()
    roomno=forms.TextInput()
    year=forms.TextInput()
    fromdate=forms.TextInput()
    fromtime=forms.TextInput()
    todate=forms.TextInput()
    totime=forms.TextInput()
    purpose=forms.TextInput()
    class Meta:
        model=Outpass_Details
        fields=['name','roomno','year','fromdate','fromtime','todate','totime','purpose']

class Complaint_detail_form(ModelForm):
    name=forms.TextInput()
    roomno=forms.TextInput()
    year=forms.TextInput()
    complaint=forms.TextInput()
    resolution=forms.TextInput()

    class Meta:
        model=Complaint_Details
        fields=['name','roomno','year','complaint','resolution']

class Admin_Outpass_detail_form(ModelForm):
    name=forms.TextInput()
    roomno=forms.TextInput()
    year=forms.TextInput()
    fromdate=forms.TextInput()
    fromtime=forms.TextInput()
    todate=forms.TextInput()
    totime=forms.TextInput()
    purpose=forms.TextInput()

    class Meta:
        model=Admin_Outpass_Details
        fields=['name','roomno','year','fromdate','fromtime','todate','totime','purpose']

class Admin_Complaint_detail_form(ModelForm):
    name=forms.TextInput()
    roomno=forms.TextInput()
    year=forms.TextInput()
    complaint=forms.TextInput()
    resolution=forms.TextInput()

    class Meta:
        model=Admin_Complaint_Details
        fields=['name','roomno','year','complaint','resolution']
