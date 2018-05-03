from django.db import models

class Client(models.Model):

    c_id     = models.CharField (max_length = 150)
    name     = models.CharField (max_length = 50)
    surname  = models.CharField (max_length = 100)
    email    = models.CharField (max_length = 100)
    phone    = models.CharField (max_length = 120)
    reg_date = models.CharField (max_length = 20)
    rating   = models.CharField (max_length = 20, default='0')
    refused_orders = models.CharField (max_length = 20, default='0')
    completed_orders = models.CharField (max_length = 20, default='0')

    @property
    def full_title(self):
        return '{0.c_id} {0.name} {0.surname} {0.phone} {0.rating}'.format(self)


    def __str__(self):
        return '{0.c_id} {0.name} {0.surname} {0.phone}'.format(self)
