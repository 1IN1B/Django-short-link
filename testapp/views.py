from django.shortcuts import render
from django.shortcuts import redirect
from testapp.models import URL
from random import *
# Create your views here.
def URL_SHORTNER_VIEW(request):
    if request.method == 'POST':
       input = request.POST["input_url"]
       alphabets = 'abcdefghijklmnopqrstuvwxyz'
       digits = '0123456789'
       output = choice(alphabets)+choice(digits)+choice(alphabets)+choice(digits)+choice(alphabets)+choice(digits)
       new_object = URL(url=input,hidden_url=output)
       new_object.save()
       return render(request,'result.html',{"output":output})
    else:
       return render(request,'home.html',{})

def About_us(request):
    return render(request,'about.html',{})

def API(request):
    return render(request,'api.html',{})

def Redirect(request,hidden_url):
    query= URL.objects.get(hidden_url=hidden_url)
    redirect_url = query.url
    return redirect(redirect_url)