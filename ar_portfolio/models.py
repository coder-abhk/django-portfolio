from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=30, null=False)
    subject = models.CharField(max_length=30, null=False)
    message = models.TextField(max_length=200, null=False)

    def __str__(self):
        return self.name