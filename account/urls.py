from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='account'#redirect 사용시 주의

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name= 'account/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mybook/',views.mybook,name='mybook'),
]