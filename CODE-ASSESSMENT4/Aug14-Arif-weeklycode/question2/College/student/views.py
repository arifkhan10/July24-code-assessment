from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addStudent(request):
    if (request.method=="POST"):
        getName=request.POST.get("name")
        getadmissionNumber=request.POST.get("admno")
        getroll=request.POST.get("roll")
        getcollege=request.POST.get("college")
        getparentName=request.POST.get("parentName")
        mydict={"name":getName,"admno":getadmissionNumber,"roll":getroll,"college":getcollege,"parentName":getparentName}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("not allowed")
# Create your views here.
