from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'ytproject'

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('video_download', views.video_download, name='video_download'),
    path('audio_download', views.audio_download, name='audio_download'),
    path('done', views.done, name='done'),
    path('', views.main, name='main'),
    
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="templates/reset_password.html"), name='reset_password'),
    
    path('reset_password_done', auth_views.PasswordResetDoneView.as_view(template_name="templates/reset_password_done.html"), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>', auth_views.PasswordResetView.as_view(), name='password_reset_confirm'),
    
    path('reset_password_complete', auth_views.PasswordResetView.as_view(template_name="templates/reset_password_complete.html"), name='password_reset_complete'),
]





