from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name='title', max_length=40)
    writer = models.TextField(verbose_name='writer', blank=True, null=True)
    content = models.TextField(verbose_name='content', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='photo1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='photo2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='photo3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Article'

    def __str__(self):
        return self.title