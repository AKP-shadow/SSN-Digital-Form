from django.contrib import admin
from django.urls import path,include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/',views.login,name="login"),
    path('login/outpass/', views.outpass, name='outpass'),
    path('outpassapproval/', views.outpassapproval, name='outpassapproval'),
    path('report/', views.report, name='report'),
    path('login/outpasslist/', views.outpasslist, name='outpasslist'),
    path('reportlist/', views.reportlist, name='reportlist'),
    path('submit/outpassform',views.outpassdetailsget,name='outpassdetails'),
    path('outpass/submit',views.outpassupload,name='outpasscreate'),
    path('report/submit',views.complaintupload,name='complaintcreate'),
    path('reportform/<int:oid>/', views.reportform, name='reportforid'),
    path('approvaloutpassform/<int:oid>/', views.approvaloutpassform, name='approvaloutpassforid'),
    path('adminoutpassform/<int:oid>/', views.adminoutpassform, name='adminoutpassforid'),
    path('adminopapproval/<int:aid>/', views.statusupload, name='adminopapproval')
    
]
 
# from django.contrib import admin
# from django.urls import path
# from . import views
# from books.views import Bookview,UserListview,BookDetailview,UserDetailview
# app_name='books'
# urlpatterns=[
#     #books/users_view
#     path('users_view/',views.view_users_list,name="view_user_html"),
#     #books/users/
#     path('users/',UserListview.as_view(),name="View_users"),
#     #books/users/1/
#     path('users/<int:pk>/',UserDetailview.as_view(),name="View_users_by_id"),
#     #books/
#     path('',Bookview.as_view(),name='view_books'),
#     #books/1/
#     path('<int:pk>/',BookDetailview.as_view(),name='view_books_by_id')
# ]