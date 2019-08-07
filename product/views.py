from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from accounts.models import Inputform
from .models import Comment


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


#detail.html 
def detail(request,board_id):
    boards = get_object_or_404(Inputform,pk=board_id)
    return render(request, 'detail.html', {'boards' : boards})


#댓글(사용안하는중)
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
     

    
