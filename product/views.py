from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from accounts.models import Inputform
from .models import Comment

# Create your views here.
def homee(request):
    return render(request, 'detail.html')
    

#board.html

def boardlist(request):
    boardlist.title = request.GET['title']
    boardlist.product_name = request.GET['product_name']
    boardlist.price = request.GET['price']
    boardlist.person_num = request.GET['person_num']
    boardlist.save()
    return redirect('/board/' + str(board.id))

def board(request):
    boards = Inputform.objects
    return render(request, 'board.html', {'boards':boards})




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
        
    
