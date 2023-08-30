from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='personal_portfolio/images')
    url = models.URLField(blank=True)
