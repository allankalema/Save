from django.urls import path 
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('bar-graph/', views.bar_graph_view, name='bar_graph'),
    path('pie-chart/', views.pie_chart_view, name='pie_chart'),
]