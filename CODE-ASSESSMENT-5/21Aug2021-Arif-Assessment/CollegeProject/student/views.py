from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from student.models import College
from student.serializers import CollegeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

def studentvi(request):
    return render(request,'register.html')

@csrf_exempt
def addstudent(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        std_serialize=CollegeSerializer(data=mydata)
        
        if (std_serialize.is_valid()):
            std_serialize.save()
            return JsonResponse(std_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def student_all(request):
    if(request.method=="GET"):
        k=College.objects.all()
        std_serializer=CollegeSerializer(k,many=True)
        return JsonResponse(std_serializer.data,safe=False)

@csrf_exempt
def student_single(request,fetchid):
    try:
        sh=College.objects.get(admnno=fetchid)
    
        
        if(request.method=="GET"):
            std_serialize=CollegeSerializer(sh)
            return JsonResponse(std_serialize.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            sh.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            std_serialize=CollegeSerializer(sh,data=mydata)

            if(std_serialize.is_valid()):
                std_serialize.save()
                return JsonResponse(std_serialize.data,status=status.HTTP_200_OK)

    except College.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def student_fetch(request,fid):
    try:
        sh=College.objects.get(id=fid)
    
        
        if(request.method=="GET"):
            std_serialize=CollegeSerializer(sh)
            return JsonResponse(std_serialize.data,safe=False,status=status.HTTP_200_OK)
    except College.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
