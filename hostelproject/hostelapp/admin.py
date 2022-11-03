from django.contrib import admin

from .models import Complaint_Details,Outpass_Details,Admin_Complaint_Details,Admin_Outpass_Details,Student_Details

admin.site.register(Complaint_Details)
admin.site.register(Outpass_Details)
admin.site.register(Admin_Complaint_Details)
admin.site.register(Admin_Outpass_Details)
admin.site.register(Student_Details)

