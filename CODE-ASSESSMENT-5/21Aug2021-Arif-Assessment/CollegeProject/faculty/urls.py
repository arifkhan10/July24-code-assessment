from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addfaculty,name='addfaculty'),
    path('viewall/',views.faculty_all,name='faculty_all'),
    path('view/<fid>',views.faculty_fetch,name='faculty_fetch'),
    path('view/<fetchid>',views.faculty_single,name='faculty_single'),
    path('register/',views.facultyregister,name='facultyregister'),
    path('login',views.facultylogin,name='facultylogin'),
]