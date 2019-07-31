from django.shortcuts import render
from accounts.models import Inputform
# Create your views here.
def board(request):
    return render(request, 'board.html')

#board.html 상세정보 가져오기
def detail(request):
    input_information = Inputform.objects
    return render(request, 'board.html', {'input_information' : input_information})


    
