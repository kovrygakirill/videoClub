from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250, null=True)

    object = models.Manager()

    def get_absolute_urls(self):
        return reverse('detail_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.category_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    plot = models.TextField(null=True)
    link_movie = models.CharField(max_length=100)
    like = models.PositiveIntegerField(default=0, editable=False)
    dislike = models.PositiveIntegerField(default=0, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    object = models.Manager()

    #
    # class Meta:
    #     db_table = 'AERODROMES'
    # comment = models.TextField(null=True)

    def __str__(self):
        return self.movie_name

    # pub_date = models.DateTimeField('date published')
