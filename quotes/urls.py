from django.urls import path

from . import views

app_name = "quotes"
urlpatterns = [
    path('', views.main, name="main"),
    path('author/<int:_id>/', views.author_info, name='author_info'),
    path('new_quote', views.add_quote, name='new_quote'),
    path('new_author', views.add_author, name='new_author'),
]
