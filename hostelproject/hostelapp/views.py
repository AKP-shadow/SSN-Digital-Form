
from audioop import reverse
from unicodedata import name
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import OutpassSerailizer,ComplaintSerailizer
from .models import Admin_Outpass_Details, Outpass_Details,Complaint_Details, Student_Details
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .forms import Admin_Complaint_detail_form, Admin_Outpass_detail_form, Outpass_detail_form,Complaint_detail_form
from .models import Outpass_Details
def home(request):
    return render(request,"Home.html")
def index(request):
    return render(request,'index.html')
def outpasslist (request):
    
    admin_outpass_list=Admin_Outpass_Details.objects.all()
    return render(request,'Outpass-List.html',{'admin_outpass_list':admin_outpass_list})
def reportlist (request):
    report_list=Complaint_Details.objects.all()
    return render(request,'Report-List.html',{'report_list':report_list})
def reportform(request,oid):
    object = Complaint_Details.objects.filter(id=oid).first()
    return render(request, "Report-Form.html", {'object':object})
def adminoutpassform(request,oid):
    
    object = Admin_Outpass_Details.objects.filter(id=oid).first()
   
   
    return render(request, "Admin_Approve_Outpass.html", {'object':object})
def approvaloutpassform(request,oid):
    object = Outpass_Details.objects.filter(id=oid).first()
    return render(request, "Outpass-Form.html", {'object':object})
def outpassapproval (request):
    outpass_list=Outpass_Details.objects.all()

    
    return render(request,'Outpass-Approval.html',{'outpass_list':outpass_list})
def outpass (request):
    
    return render(request,'Outpass.html')

def report(request):
   
    return render(request,'Report.html')

@csrf_exempt
def outpassupload(request):
    if (request.method=='POST'):
        form=Outpass_detail_form(request.POST,request.FILES)
        admin_form=Admin_Outpass_detail_form(request.POST,request.FILES)
        
        
        # print(Student_Details.objects,"rrage",Student_Details.objects.get(regno="1234"))
        # stu=Student_Details.objects.get(email="gfbgfgnngf")
        # print(stu)
        # stu.name="agregegq"
        # stu.save()

        # obj=Outpass_Details.objects.all()
        # stu_form=Student_Details_form(request.POST,request.FILES)
        # student=form.save(commit=False)
        # objs=form.cleaned_data['outpass']
        # student.save()

        # student.obj.set(objs)




        if form.is_valid():  
            form.save()    
            admin_form.save()
        # upobj=Outpass_Details.objects.get(name=request.POST['name'])
        # stu=Student_Details.objects.create(id=1)
        # stu.save()
        # stu.outpass.add(upobj)
    
        

        
    return render(request,'Outpass-Form.html')

def outpassdetailsget(request):
    outpass_list=Outpass_Details.objects.all()
    
    return render(request,'Outpass-List.html',{'outpass_list':outpass_list})

@csrf_exempt
def complaintupload(request):
    if (request.method=='POST'):
        form=Complaint_detail_form(request.POST,request.FILES)
        admin_form=Admin_Complaint_detail_form(request.POST,request.FILES)
        # john = Outpass_Details.objects.create(name="John")
        # paul = Outpass_Details.objects.create(name="Paul")
        # george = Outpass_Details.objects.create(name="George")
        # ringo = =Outpass_Details.objects.create(name="Ringo")
        # entry.authors.add(john, paul, george, ringo)
        # request.POST[]
        
        if form.is_valid():  
            form.save()
        if admin_form.is_valid():    
            admin_form.save()
        context={'reportform':Complaint_detail_form,
                'adminreportform':Admin_Complaint_detail_form}
    return render(request,'Report.html',context)

@csrf_exempt
def statusupload(request,aid):
    
    if (request.method=='POST'):
        
        print(request.POST)
        
        object = Admin_Outpass_Details.objects.filter(id=aid).first()
        upobj=Outpass_Details.objects.get(name=object.name)
        if(request.POST['submitclicked']=="Decline"):
            upobj.status="Decline"
        elif(request.POST['submitclicked']=="Approve"):
            upobj.status="Approve"
        upobj.save()
        object.delete()
    return render(request,"Outpass-List.html")

@csrf_exempt
def login(request):
    # return HttpResponseRedirect('outpasslist')
    if (request.method=='POST'):
        print(request.POST)
        stu=Student_Details.objects.get(email=request.POST['email'])
        print(stu,request.POST['email'])
        if(request.POST['password']==stu.password):
            if(request.POST['email']=="admin@ssn.edu.in"):
                print(stu,request.POST['email'])
                return HttpResponseRedirect('outpasslist',{'stu':stu})
            else:
                return HttpResponseRedirect('outpass',{'stu':stu})

        # return HttpResponseRedirect('home',{'stu':stu,})
    

# @csrf_exempt
# class OutpassCreateview(generics.ListCreateAPIView):
#     queryset=Outpass_Details.objects.all()
#     serializer_class=OutpassSerailizer
# @csrf_exempt
# class ComplainCreateview(generics.ListCreateAPIView):
#     queryset=Complaint_Details.objects.all()
#     serializer_class=ComplaintSerailizer
# @csrf_exempt
# class OutpassDetailsView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'Outpass.html'
#     def get(self,request):
#         outpass_list=Outpass_Details.objects.all()
#         serializer=OutpassSerailizer(outpass_list)
#         return Response(serializer.data)
    # def post(self, request):
       
    #     serializer = 
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'profile': profile})
    #     serializer.save()
    #     return redirect('profile-list')
# class ComplainDetailsView(APIView):
#     def get(self,request):
#         complain_list=Complaint_Details.objects.all()
#         serializer=ComplaintSerailizer(complain_list)
#         return Response(serializer.data)

# class ComplainDetailsView(APIView):
#     def get(self,request):
#         complain_list=Complaint_Details.objects.all()
#         serializer=ComplaintSerailizer(complain_list)
#         return Response(serializer.data)


# def view_users_list(request):
#     user_data=User.objects.all()
#     user_template=loader.get_template("UserDetails.html")
#     context={"books_users_data":user_data}
#     html_data=user_template.render(context)
#     return HttpResponse(html_data)


# class UserListview(generics.ListCreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerailizer
# class UserDetailview(generics.RetrieveUpdateDestroyAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerailizer
# class Bookview(APIView):
#     def get(self,request):
#         book_list=Book.objects.all()
#         serializer=BookSerailizer(book_list,many=True)
#         return Response(serializer.data)
# class BookDetailview(APIView):
#     def get(self,request,pk):
#         book_list=Book.objects.get(pk=pk)
#         serializer=BookSerailizer(book_list)
#         return Response(serializer.data)


# @csrf_exempt
# def OutpassApi(request,id=0):
#     if request.method=='GET':
#         complain_list = Outpass_Details.objects.all()
#         complaint_serializer=OutpassSerailizer(complain_list,many=True)
#         return JsonResponse(complaint_serializer.data,safe=False)
#     elif request.method=='POST':
#         complain_list=JSONParser().parse(request)
#         complaint_serializer=OutpassSerailizer(data=complain_list)
#         if complaint_serializer.is_valid():
#             complaint_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         complain_list=JSONParser().parse(request)
#         complaint=Outpass_Details.objects.get(DepartmentId=complain_list['DepartmentId'])
#         complaint_serializer=OutpassSerailizer(complaint,data=complain_list)
#         if complaint_serializer.is_valid():
#             complaint_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         complain_list=Outpass_Details.objects.get(DepartmentId=id)
#         complain_list.delete()
#         return JsonResponse("Deleted Successfully",safe=False)
