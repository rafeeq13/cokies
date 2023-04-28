from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def setsignedcookie(request):  
    response = render(request,'enroll/setcookie.html')  
    response.set_signed_cookie('name','rafeeq',salt='nm',expires=10)
    return response

def getsignedcookie(request):
    #nm=request.COOKIES['name']
    nm=request.get_signed_cookie('name',salt='nm',default='guest')
    return render(request,'enroll/getcookie.html',{'name':nm})
def delcookie(request):
    response = render(request,'enroll/delcookie.html')  
    response.delete_cookie('name')
    return response
