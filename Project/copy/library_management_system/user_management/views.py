from django.shortcuts import render

def guest(request):
    return render(request, 'user_management/index_user.html')
def about_us(request):
    return render(request, 'user_management/about_us.html')
def contact_us(request):
    return render(request, 'user_management/contact_us.html')
def profile(request):
    return render(request, 'user_management/profile.html')
def login(request):
    return render(request, 'user_management/login.html')
def user_login(request):
    return render(request, 'user_management/user_login.html')

