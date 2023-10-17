from django.urls import path
from .views import PostView, FileDownloadView, Last15PostsView,PostSingeSearch

urlpatterns = [
    # Your other URL patterns
    path('posts/download/<int:pk>', FileDownloadView.as_view(), name='file-download'),
    path('posts/', PostView.as_view(), name='post_api'),
    path('search/<int:pk>', PostSingeSearch.as_view(), name='post_api'),
    path('posts/new', Last15PostsView.as_view(), name='last-15-posts-api'),
]
