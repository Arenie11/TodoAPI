from django.urls import path
from . import views
urlpatterns= [
    path('gettodo/', views.TodoView.as_view()),
    path('<str:id>/', views.SingleTodoView.as_view()),
    path('register/', views.RegistrationView.as_view()),
]