from django.urls import path, include
from xlapp import views

urlpatterns = [

    path('/a', views.xl, name='xl'),
    path('<int:well>', views.show, name='show'),
]