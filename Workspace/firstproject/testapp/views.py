from django.shortcuts import render
from django.http import HttpResponse
def greeting(request):
    menu="""
         <a href="http://localhost:8000/testapp/hello">Home</a>
         <a href="http://localhost:8000/testapp/about">About</a>
         <a href="http://localhost:8000/testapp/contacts">Contacts</a>
    """   
    s="<h1>Welcome to first django project</h1>"
    s=menu+s
    return HttpResponse(s)
def about(request):
     menu="""
         <a href="http://localhost:8000/testapp/hello">Home</a>
         <a href="http://localhost:8000/testapp/about">About</a>
         <a href="http://localhost:8000/testapp/contacts">Contacts</a>
    """    
     s="<h1>About Page</h1>"
     s=menu+s
     return HttpResponse(s)    
def contacts(request):
     menu="""
         <a href="http://localhost:8000/testapp/hello">Home</a>
         <a href="http://localhost:8000/testapp/about">About</a>
         <a href="http://localhost:8000/testapp/contacts">Contacts</a>
    """            
     s="<h1>Contacts Page</h1>"
     s=menu+s
     return HttpResponse(s)     