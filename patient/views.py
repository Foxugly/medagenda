from django.shortcuts import render
from patient.models import Patient
from django.http import HttpResponse
import json

# Create your views here.
def search_patient(request):
    if request.is_ajax():
        email = request.GET['email']
        print email
        if len(email)>5:
            p = Patient.objects.filter(email=email)
            if p:
                return HttpResponse(json.dumps({'return':True, 'patient':p}))
            else:
                return HttpResponse(json.dumps({'return':False}))
        else:
            return HttpResponse(json.dumps({'return':False}))
