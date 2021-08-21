from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addstudent,name='addstudent'),
    path('viewall/',views.student_all,name='event_all'),
    path('view/<fid>',views.student_fetch,name='student_fetch'),
    path('view/<fetchid>',views.student_single,name='student_single'),
    path('student/',views.studentvi,name='studentvi'),
]