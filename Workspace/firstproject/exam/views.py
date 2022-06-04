from django.shortcuts import render
from django.http import HttpResponse
from .models import Addcontact
#from django.contrib import messages
#from django.db import models
def testPaper(request):
    q="Who developed C-Language?"
    a="Ken Thomson"
    b="Dennis Ritchie"
    c="Bjarne Stroustrup"
    d="Guido Van Rossum"
    d1={'que':q,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/show_test.html',d1)
    return res
def testResult(request):
    s="Test-Result"
    return HttpResponse(s)    

def students(request):
    allData = Addcontact.objects.all()
    data={
        'allData':allData

    }
    return render(request,'contacts_data.html',data)   