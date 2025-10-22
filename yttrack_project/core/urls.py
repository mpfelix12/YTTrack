from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('quadros/', views.quadros, name='quadros'),
    path('quadros/novo/', views.novo_quadro, name='novo_quadro'),
    # (as próximas rotas de quadros/vídeos serão adicionadas nas etapas seguintes)
]
