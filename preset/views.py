from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import FileResponse
from .models import post,Catagores
from .serializer import PostSerializer,CatagoiresSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from django.http import Http404  # Import Http404 to handle file not found

class FileDownloadView(APIView):
    def get(self, request, pk):
        try:
            post_obj = post.objects.get(pk=pk)
            if post_obj.fileupload:
                file_path = post_obj.fileupload.path
                content_type = 'application/octet-stream'  # Specify the correct content type
                filename = post_obj.fileupload.name
                response = FileResponse(open(file_path, 'rb'), content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            else:
                raise Http404("No file found for this post")
        except post.DoesNotExist:
            return Response({"error": "Post not found."}, status=404)



class PostView(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class SearchPostsByTitle(APIView):
    def get(self, request):
        search_term = request.query_params.get('title', '')
        queryset = post.objects.filter(title__icontains=search_term)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class Last15PostsView(APIView):
    def get(self, request):
        last_posts = post.objects.all().order_by('-id')[:20]
        serializer = PostSerializer(last_posts, many=True)
        return Response(serializer.data)

# catagories wise post

class CategoryPostListView(APIView):
    def get(self, request, catagories_id):
        try:
            queryset = post.objects.filter(catagories__id=catagories_id)
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CatagoryListVIew(generics.ListAPIView):
        queryset = Catagores.objects.all()
        serializer_class = CatagoiresSerializer


