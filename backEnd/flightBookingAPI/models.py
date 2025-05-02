from django.db import models


class Flights(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    ucode = models.IntegerField()
    hcode = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    # Define the t a b l e name
    class Meta:
        db_table = 'flights'