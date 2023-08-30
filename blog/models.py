from django.db import models

# Create your models here.
class Model(models.Model):
    image = models.ImageField(upload_to='blog_image', blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title