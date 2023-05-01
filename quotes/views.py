# Create your views here.
from django.shortcuts import render


def main(request):
    return render(request, 'quotes/base.html', context={})
