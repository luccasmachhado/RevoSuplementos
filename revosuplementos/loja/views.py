from django.shortcuts import render

# Create your views here.
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos})