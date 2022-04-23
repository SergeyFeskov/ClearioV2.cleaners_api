from django.db import models

class CleanersInfo(models.Model):
    # id = models.IntegerField(primary_key=True, null=False, unique=True, auto_created=True)
    id = models.BigAutoField(primary_key=True, null=False, unique=True, auto_created=True)
    name = models.CharField(max_length=60, blank=False)
    surname = models.CharField(max_length=60, blank=False)
    city = models.CharField(max_length=60, blank=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=60, blank=False)
    isworking = models.BooleanField(db_column='isWorking', default=False)
    rating = models.IntegerField(default=0)


    class Meta:
        managed = False
        db_table = 'cleanersInfo'

    def __str__(self):
        return f"ID {self.id}: {self.name} {self.surname} ({self.phonenumber})"
