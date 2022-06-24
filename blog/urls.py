from django.urls import path
from .views import BlogCreateView, BlogDeleteView, BlogListView, BlogDetailView, BlogUpdateView
app_name = 'blog'
urlpatterns = [
   path('list/',BlogListView.as_view(), name='blog_list'),
   path('create/',BlogCreateView.as_view(), name='blog_create'),
   path('<int:pk>/detail',BlogDetailView.as_view(), name='blog_detail'),
   path('<int:pk>/update/',BlogUpdateView.as_view(), name='blog_update'),
   path('<int:pk>/delete/',BlogDeleteView.as_view(), name='blog_delete'),
]