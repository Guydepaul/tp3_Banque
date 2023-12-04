from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil_view, name='accueil'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('deposer/', views.deposer_view, name='deposer'),
    path('retirer/', views.retirer_view, name='retirer'),
]
