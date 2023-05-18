from django.db import models

# Create your models here.
class tasklist(models.Model):
    heading = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    datatime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading