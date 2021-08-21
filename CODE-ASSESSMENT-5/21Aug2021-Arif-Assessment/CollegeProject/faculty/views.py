from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from faculty.models import Faculty
from faculty.serializers import FacultySerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

def facultylogin(request):
    return render(request,'login.html')

def facultyregister(request):
    return render(request,'registerf.html')

@csrf_exempt
def addfaculty(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(data=mydata)
        
        if (faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def faculty_all(request):
    if(request.method=="GET"):
        k=Faculty.objects.all()
        faculty_serializer=FacultySerializer(k,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)

@csrf_exempt
def faculty_single(request,fetchid):
    try:
        sh=Faculty.objects.get(fcode=fetchid)
    
        
        if(request.method=="GET"):
            faculty_serialize=FacultySerializer(sh)
            return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            sh.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            faculty_serialize=FacultySerializer(sh,data=mydata)

            if(faculty_serialize.is_valid()):
                faculty_serialize.save()
                return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)

    except Faculty.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def faculty_fetch(request,fid):
    try:
        sh=Faculty.objects.get(id=fid)
    
        
        if(request.method=="GET"):
            faculty_serialize=FacultySerializer(sh)
            return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
    
    except Faculty.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)


