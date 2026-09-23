from django.db import models

# Create your models here.




class Author(models.Model):
    name = models.CharField(max_length=50,default="",blank=False)
    bio = models.TextField(max_length=600,default="",blank=True)

        
    def __str__(self):
        return self.name



class Publisher(models.Model):
    name = models.CharField(max_length=50,default="",blank=False)

    
    def __str__(self):
        return self.name




class Genre(models.Model):
    name = models.CharField(max_length=30,default="",blank=False)

    
    def __str__(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=50 , default="",blank=False)
    isbn = models.CharField(max_length=14,default="",blank=False)
    description = models.TextField(max_length=600, default="", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ManyToManyField(Author,related_name="books")
    publisher = models.ForeignKey(Publisher,null=True,on_delete=models.SET_NULL,related_name="books")
    genres = models.ManyToManyField(Genre,related_name="books")

    
    def __str__(self):
        return self.title





