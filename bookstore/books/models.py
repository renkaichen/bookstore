from django.db import models
class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    cover = models.ImageField(upload_to='book_covers/')
    def __str__(self):
        return str(self.isbn) + ' - ' + self.title
# Create your models here.
