from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('topics/', views.topicsPage, name="topics"),
    path('signup',views.signup,name="signup"),
    path('login',views.handalelogin,name="login"),
    
]