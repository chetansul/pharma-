from django.shortcuts import render

# Create your views here.
def profiles(request):
    return render(request,'user/profile.html')

