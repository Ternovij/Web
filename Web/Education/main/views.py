from django.shortcuts import render
# Create your views here.

def index(reguest):
    return render(reguest,'main/index.html')

def about(reguest):
    return render(reguest,'main/about.html')