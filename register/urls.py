from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'register'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', views.dashboard, name='dashboard'),
    # password change views 

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    # password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset_request.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('', views.signup, name='signup'),
    path('success/', views.signup_success, name='success'),
]
