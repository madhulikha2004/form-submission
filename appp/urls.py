from django.urls import path
from appp import views
urlpatterns=[
    path('mash/',views.func1),
    path('nash/',views.func2),
    path('lash/',views.func3),
    path('oash/',views.func4)
]