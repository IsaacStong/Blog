from django.urls import path, include
from .views import HomeView, PostDetailView, CreatePost, UpdatePost, DeletePost, CategoryPage

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post_details/<int:pk>', PostDetailView.as_view(), name='post_details'),
    path('post_create/', CreatePost.as_view(), name='create'),
    path('post_edit/<int:pk>', UpdatePost.as_view(), name='edit'),
    path('post_delete/<int:pk>', DeletePost.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryPage.as_view(), name='category')
]
