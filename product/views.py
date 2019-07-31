from django.shortcuts import render
from .models import Inputform
# Create your views here.
def board(request):
    return render(request, 'board.html')