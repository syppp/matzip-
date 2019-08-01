from django.contrib import admin
from django.urls import path
import accounts.views
import product.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.home, name="home"),
    path('input', accounts.views.input, name="input"),
    path('inputform', accounts.views.inputform, name="inputform"),
    path('detail', accounts.views.detail, name="detail"),
    path('login', accounts.views.login, name="login"),
    path('register', accounts.views.register, name="register"),
    path('board', product.views.board, name="board"),#product->account로 바꿈
    #path('board/<int: input_id>/', product.views.homee, name="detail"),#요놈바꿈
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
