from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def setcookie(request):  
    response = render(request,'enroll/setcookie.html')  
    response.set_cookie('name','sonam')
    return response

def getcookie(request):
    #nm=request.COOKIES['name']
    nm=request.COOKIES.get('name')
    return render(request,'enroll/getcookie.html',{'name':nm})
def delcookie(request):
    response = render(request,'enroll/delcookie.html')  
    response.delete_cookie('name')
    return response
