from django.contrib import admin
from django.urls import path
import accounts.views
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.home, name="home"),
    path('input', accounts.views.input, name="input"),
    path('inputform', accounts.views.inputform, name="inputform"),
    path('detail', accounts.views.detail, name="detail"),
    path('login', accounts.views.login, name="login"),
    path('register', accounts.views.register, name="register"),
    path('detail', product.views.board, name="detail"),
    path('create',product.views.create, name='create')
]
