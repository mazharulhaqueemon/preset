from django.urls import path
from .views import PostView, FileDownloadView, Last15PostsView, CategoryPostListView, SearchPostsByTitle

urlpatterns = [
    # Your other URL patterns
    path('posts/download/<int:pk>', FileDownloadView.as_view(), name='file-download'),
    path('posts/', PostView.as_view(), name='post_api'),
    path('search/', SearchPostsByTitle.as_view(), name='post_api'),
    path('posts/new', Last15PostsView.as_view(), name='last-15-posts-api'),
    path('category/<int:catagories_id>/posts/', CategoryPostListView.as_view(), name='category-post-list'),
]
