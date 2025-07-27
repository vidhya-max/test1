from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    msg='welcome to django'
    return HttpResponse(msg)
def index(request):
    
    return HttpResponse('<h1>welcometo index page</h1>')
def fun(request):
    return render(request,'index.html')