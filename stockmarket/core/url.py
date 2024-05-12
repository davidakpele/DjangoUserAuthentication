from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
# setting url
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('add/', views.add_record, name='add'),
    path('show/', views.get_all_users, name='show'),
    path('auth/login', views.user_login, name='auth/login'),
    path('api/updat/records', views.updateUser_stockMarkert, name='api/updat/records'),
    path('dashboard/index/', views.default, name='dashboard/index'),
    path('logout/', views.logout_view, name='logout'),
    
]