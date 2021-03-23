from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=20)
    network = models.CharField(max_length=20)
    date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
