from django.urls import path,include
from . import views

urlpatterns = [
    path('log',views.logfunction,name='log'),
    path('forget',views.forgetfunction,name='forget'),
    

   
]