from django.db import models
from catalog.models import Book
from accounts.models import User
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="review")
    book = models.ForeignKey(Book,null=True,on_delete=models.CASCADE,related_name="reviews")
    rrating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(max_length=1000,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.book}{self.user}{self.rating}"
    



class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="favorite")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="favorite_by")

    
    def __str__(self):
        return f"{self.user} {self.book}"

    

