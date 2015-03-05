from django.db import models


class UserData(models.Model):
    member_id = models.IntegerField(unique=True)
    generic_shift = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return "%s" % self.member_id


class Shift(models.Model):
    user_data = models.ForeignKey(UserData, related_name='shifts')
    end = models.CharField(max_length=128)
    expiration = models.CharField(max_length=128)
    member = models.IntegerField()
    origShiftId = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    shiftId = models.CharField(max_length=128)
    start = models.CharField(max_length=128)

