from django.db import models
from datetime import date, datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show title MUST be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Show network MUST be at least 3 characters"
        if len(postData['desc']) < 10:
            errors['desc'] = "Show description MUST be at least 10 characters"
        create_date = datetime.strptime(postData['date'], '%Y-%m-%d')
        today = datetime.today()
        if create_date > today:
            errors['past_date'] = "Date must be in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=20)
    network = models.CharField(max_length=20)
    date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __str__(self):
        return self.title
