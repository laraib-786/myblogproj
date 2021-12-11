from django.shortcuts import render

# Create your views here.
# i have written this
def home_view(request):
    return render(request,'static_pages/index.html')
