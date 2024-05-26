from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('community/',views.community,name='community'),
    path('aboutus/',views.about,name='aboutus'),
    path('emotion_intelligence',views.face_ai,name='face_ai'),
    path('entertainment/',views.entertainment,name='entertainment'),
]
