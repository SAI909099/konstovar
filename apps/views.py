from django.shortcuts import render
from django.shortcuts import render

def my_view(request):
    return render(request, 'apps/index.html')



