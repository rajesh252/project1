from django.shortcuts import render

# Create your views here.
def puppy(request):
    return render(request, 'puppy.html')