from djongo import models
from djongo.models import fields, DjongoManager

# Create your models here.
        
class BookModel(models.Model):
    
    title = models.TextField()
    author = models.TextField()
    class Meta:
        db_table = 'books'