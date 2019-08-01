from django.shortcuts import render,get_object_or_404
from accounts.models import Inputform
from .models import Comment
#def homee(request,input_id):
#input_detail = get_object_or_404(Inputform,pk=input_id)
#return render(request, 'detail.html',{'input_detail':input_detail})

#board.html
def board(request):
    return render(request, 'board.html',)
#detail.html 
def detail(request,input_id):
    input_information = get_object_or_404(Inputform,pk=input_id)
    return render(request, 'detail.html', {'input_information' : input_information})


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
     

    
