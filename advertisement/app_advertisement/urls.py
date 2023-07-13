from django.urls import path
from .views import index,top,post,reg,login,profile
urlpatterns = [
    path('', index,name='/'),
    path('top-sell',top,name='top'),
    path('post',post,name='post'),
    path('reg',reg,name='reg'),
    path('login',login,name='log'),
    path('profile',profile,name='profile'),

]
