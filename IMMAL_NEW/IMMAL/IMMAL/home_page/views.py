from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home_page/home.html')

def about(request):
    return render(request,'home_page/aboutus.html')

def face_ai(request):
    return render(request,'home_page/face_emotion_ai.html')

def entertainment(request):
    return render(request,'home_page/entertainment.html')

def community(request):
    return render(request,'home_page/community.html')