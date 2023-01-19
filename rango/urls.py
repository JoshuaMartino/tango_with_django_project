from django.urls import  path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('picture/', views.picture, name= "picture"),
    path('about/',views.about, name = "about" ),
]