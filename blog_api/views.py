from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from blog.models import Post
from .serializers import PostSerializers
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Hello, World!")

class PostApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):
        thisPost = Post.objects.get(title=request.user)
        serializer = PostSerializers(thisPost,many = False)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    def post(self,request, *args, **kwargs):
        data = {
            'title':request.data.get('title'),
            'body':request.data.get('body'),
            'author':request.data.get('author')
        }
        serializer = PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )