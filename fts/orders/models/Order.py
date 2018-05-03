from django.db import models
from .Direction import Direction, Urgency, Status
from translator.models import Translator
from ..utils.Utils import validate_file_extension, content_file_name


class Order(models.Model):

    o_id = models.CharField(max_length=15, unique=True)
    lang = models.CharField(max_length=50)
    pages = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    direction = models.CharField(max_length=20)
    urgency = models.CharField (max_length=10, default="2")
    customer = models.CharField (max_length=15)
    translated = models.OneToOneField(Translator, on_delete=models.CASCADE,  null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,  null=True, blank=True)
    file_path = models.CharField(max_length=100, default='unknown')


    @property
    def full_title(self):
        return '{0.o_id} {0.lang} {0.pages} {0.urgency} {0.price} {0.customer} {0.translator} {0.status}'.format(self)

    def __str__(self):
        return '{0.o_id} {0.lang} {0.price} {0.urgency} {0.status}'.format(self)


class Files(models.Model):

    ord_id = models.CharField(max_length=15)
    ord_file = models.FileField(upload_to=content_file_name)

    @property
    def path_to_files(self):
        return content_file_name
