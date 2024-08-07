from djongo import models
from djongo.models import fields, DjongoManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
        
class BookModel(models.Model):

    class StatusType(models.TextChoices):
        INACTIVE = "0", "Inactive"
        ACTIVE = "1", "Active"

    _id = models.ObjectIdField()
    title = models.CharField(max_length=150)
    author = models.TextField(max_length=200)
    isbn = models.CharField(max_length=100,unique=True)
    published_date = models.PositiveBigIntegerField()
    genre = models.TextField(max_length=50)
    description = models.TextField(max_length=1000,null=True)
    copies_available = models.PositiveIntegerField()
    total_copies = models.PositiveIntegerField()
    publisher = models.TextField(null=True)
    language = models.TextField(max_length=30)
    keywords = models.JSONField(default=list)
    shelf_location = models.CharField(max_length=250)
    added_date = models.PositiveBigIntegerField()
    last_updated_date = models.PositiveBigIntegerField(null=True)
    status = models.CharField(max_length=1,choices=StatusType.choices,default=StatusType.ACTIVE)
    class Meta:
        db_table = 'books'