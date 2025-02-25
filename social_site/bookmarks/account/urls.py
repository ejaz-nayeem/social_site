from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    #path('logout-then-login', auth_views.LogoutThenLoginView.as_view(), name='logout-then-login'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-change', auth_views.PasswordChangeView.as_view(), name='password_change'),
]
