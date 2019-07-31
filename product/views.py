from django.shortcuts import render
from accounts.models import Inputform
from .models import Comment
# Create your views here.
def board(request):
<<<<<<< HEAD

    return render(request, 'board.html')
=======
    return render(request, 'detail.html')
>>>>>>> 909403ea0d39ab6b4b10a8488afee50760210fb4


#board.html 상세정보 가져오기
def detail(request):
    input_information = Inputform.objects
    return render(request, 'detail.html', {'input_information' : input_information})

#댓글
def home(request):
    
    comment=Comment.objects
    return render(request, 'detail.html', {'comment':comment}) 
def create(request):
    com = Comment()
    com.comment_date = timezone.datetime.now()
    com.comment_user = request.GET['name']
    com.comment_textfield = request.GET['context']
    com.save()
    return redirect('/')
        
    
