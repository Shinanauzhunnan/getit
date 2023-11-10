from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=255)
    blog = models.CharField(max_length=1024)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
