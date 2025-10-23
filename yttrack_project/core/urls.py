from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('quadros/', views.quadros, name='quadros'),
    path('quadros/novo/', views.novo_quadro, name='novo_quadro'),
    
    path('quadros/<int:pk>/videos/', views.videos_por_quadro, name='videos_por_quadro'),
    path('videos/<int:pk>/toggle_watched/', views.toggle_watched, name='toggle_watched'),

    path('quadros/<int:pk>/videos/novo/', views.novo_video, name='novo_video'),

    # (as próximas rotas de quadros/vídeos serão adicionadas nas etapas seguintes)
]
