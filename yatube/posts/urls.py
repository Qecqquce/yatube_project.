from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='general_page'),
    path('group_list/<slug:slug>/', views.group_posts, name='group_posts'),

]
