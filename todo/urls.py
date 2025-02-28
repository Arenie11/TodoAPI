from django.urls import path
from . import views
urlpatterns= [
    path('gettodo/', views.TodoView.as_views()),
    path('<str:id>/', views.SingleTodoView.as_views()),
    path('<register/', views.RegistrationView.as_views()),
]