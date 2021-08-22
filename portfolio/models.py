from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
