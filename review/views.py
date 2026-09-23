
from rest_framework.response import Response
from .serializers import FavoriteSerializer,ReviewSerializer
from .models import Favorite , Review
from rest_framework.decorators import api_view ,permission_classes
from rest_framework import status,generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly




class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)