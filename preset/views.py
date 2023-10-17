from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import FileResponse
from .models import post
from .serializer import PostSerializer


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

class PostSingeSearch(generics.RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer




class Last15PostsView(APIView):
    def get(self, request):
        last_posts = post.objects.all().order_by('-id')[:20]
        serializer = PostSerializer(last_posts, many=True)
        return Response(serializer.data)


