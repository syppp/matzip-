from django.shortcuts import render
from accounts.models import Inputform
from .models import Comment
# Create your views here.
def homee(request):
    return rener(request, 'detail.html')
    
def board(request):
    return render(request, 'board.html')

#detail.html 상세정보 가져오기
def detail(request):
    input_information = Inputform.objects
    return render(request, 'detail.html', {'input_information' : input_information})

#댓글
def home(request):
    comment = Comment.objects
    return render(request, 'detail.html', {'comment':comment}) 

def create(request):
    com = Comment()
    com.comment_date = timezone.datetime.now()
    com.comment_user = request.GET['name']
    com.comment_textfield = request.GET['context']
    com.save()
    return redirect('/')
        
    
