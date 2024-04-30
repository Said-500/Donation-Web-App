from django.db import models

class user_data(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,default="1234")


    class Meta:
        db_table = 'user_data-table'
