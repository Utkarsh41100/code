from django.shortcuts import render

def guest(request):
    return render(request, 'guest_management/index_guest.html')
def about_us(request):
    return render(request, 'guest_management/about_us.html')
def contact_us(request):
    return render(request, 'guest_management/contact_us.html')
def profile(request):
    return render(request, 'guest_management/profile.html')
def login(request):
    return render(request, 'guest_management/login.html')

