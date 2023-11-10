from django.urls import path
from .views import index, login, logout

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
    
]