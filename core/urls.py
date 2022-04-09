from django.urls import path
from .views import IndexView, DetailItemView, CreateItemView, UpdateItemView, DeleteItemView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailItemView.as_view(), name='detail_view'),
    path('create/', CreateItemView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateItemView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteItemView.as_view(), name='delete'),
]