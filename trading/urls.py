from django.urls import path
from . import views


app_name = 'trading'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:write_id>/', views.detail, name='detail'),
    path('write/create/', views.write_create, name='write_create'),
    path('answer/create/<int:write_id>/', views.answer_create, name='answer_create'),
]

