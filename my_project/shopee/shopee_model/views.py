from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    return render(request,"frontend.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact_us.html")
def privacy_policy(request):
    return render(request,"privacy_policy.html")
