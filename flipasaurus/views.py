from django.shortcuts import render

# Create your views here.

def test(request):
  return render(request, 'base.html')

def dashboard(request):
  return render(request, 'flipasaurus/dashboard.html')

