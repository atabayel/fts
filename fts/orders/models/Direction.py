from django.db import models

class Direction(models.Model):

    name =  models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '({0.name}) {0.comment}'.format(self)



class Urgency(models.Model):

    name = models.CharField(max_length=10, null=False, blank=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '({0.name}) {0.comment}'.format(self)


class Status(models.Model):

    name = models.CharField(max_length=10, null=False, blank=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '({0.name}) {0.comment}'.format(self)

