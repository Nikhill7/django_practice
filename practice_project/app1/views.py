from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    l = ["qwerty","sd", "we"]
    d = {"name":l}
    return render(request,'index.html', d)

def link(request):
    return render(request,'link.html')