from django.db import models

# Create your models here.
# 09-24
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField()


    def __str__(self):
        return f'[{self.pk}]{self.title}'