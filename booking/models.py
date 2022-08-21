from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    price = models.IntegerField(null=False)
    cover_image = models.CharField(max_length=256, null=True, blank=True)
    author = models.ForeignKey(User, related_name='books', related_query_name='books', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'
