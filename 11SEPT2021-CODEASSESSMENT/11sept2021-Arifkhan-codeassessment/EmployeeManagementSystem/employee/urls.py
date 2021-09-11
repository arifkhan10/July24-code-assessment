from django.urls import path
from . import views
urlpatterns = [
 
    path('signuppage/',views.employeeP,name='employeeP'),
    path('viewall/',views.employee_list,name='employee_list'),
    path('viewemployee/<fetchid>',views.employee_details,name='employee_details'),
    path('signup/',views.empsignup,name='empsignup'),
    path('view/',views.viewall,name='viewall'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('update/',views.empupdate,name='empupdate'),
    path('login/',views.login_check,name='login_check'),
    path('logout/',views.emplogout,name='emplogout'),
    path('loginview/',views.loginview,name='loginview'),

]