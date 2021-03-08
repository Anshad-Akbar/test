from django.urls import path,include
from . import views

urlpatterns = [
    path('sample',views.samplefunction,name='sample'),

]