from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})

def contact_view(request,*args, **kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args, **kwargs):
    my_context = {
        "my_text":"This is about us",
        "my_number":123,
        "my_list":[456,789,345,"abc def ghi"]

        }
    return render(request,"about.html",my_context)