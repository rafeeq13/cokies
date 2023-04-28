from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',views.setsignedcookie,name='setcookie'),
    path('get/',views.getsignedcookie,name='getcookie'),
    path('del/',views.delcookie,name='delcookie'),
]