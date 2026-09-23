from rest_framework import serializers
from .models import Review , Favorite
 
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model =Review
        fields = ["id", "user", "book", "rating", "comment", "created_at"]
        read_only_fields = ["id", "user", "created_at"]



class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Favorite
        fields = ["id", "user", "book", "created_at"]
        read_only = ["id","user","created_at"]
