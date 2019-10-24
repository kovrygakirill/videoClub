from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    plot = models.TextField(null=True)
    link_movie = models.CharField(max_length=100)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    #comment = models.TextField(null=True)

    def __str__(self):
        return self.movie_name

    # pub_date = models.DateTimeField('date published')
