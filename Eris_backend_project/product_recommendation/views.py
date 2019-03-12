# Create your views here.
from typing import Any
from urllib.request import Request

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from product_recommendation.models import Movie
from product_recommendation.serializers import MovieSerializer


class LBHAPIView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class MovieAPIViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any):
        request.data['movie_owner']= [request.user.id, ]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request: Request, *args: Any, **kwargs: Any):
    #     moive_owenr = request.user
    # http request create =  && 5개 있음 이런거
