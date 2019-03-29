from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    author = models.ForeignKey('Author', on_delete=models.SET_DEFAULT, default='Denis Vorko', null=True, help_text='author')
#    author = models.CharField(max_length=56, default='Denis Vorko')
    date_pub = models.DateTimeField(auto_now_add=True)
    manual = models.TextField(help_text='About this', max_length=1024, blank=True)
    image = models.ImageField(upload_to='page_denis_vorko/static/page_denis_vorko/img')

    class Meta():
        ordering = ['-date_pub']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=128, default='Denis Vorko')

    def __str__(self):
        return '{}'.format(self.name)
