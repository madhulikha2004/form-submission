from django.urls import path
from app1 import views
urlpatterns=[
    path('wish/',views.func1),
    path('vash/',views.func2)
]