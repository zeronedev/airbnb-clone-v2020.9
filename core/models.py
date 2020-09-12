from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        """ abstract(추상화) class """

        # database에 등록하지 않는다
        abstract = True
