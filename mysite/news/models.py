from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=127)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField()


    def __str__(self):
        return self.title