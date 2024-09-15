from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context={
        'Variable': "This is the value of variable "
    }
    return render(request, 'index.html',context)  ## Redirect index.html file . Context is a variable that is passed
def about(request):
    return render(request, 'about.html')
def profile(request):
    return render(request, 'profile.html')