from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt

def addFaculty(request):
    if (request.method=="POST"):
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getDepartment=request.POST.get("department")
        getcollege=request.POST.get("college")
        
        mydict={"name":getName,"address":getAddress,"department":getDepartment,"college":getcollege}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("not allowed")
# Create your views here.
