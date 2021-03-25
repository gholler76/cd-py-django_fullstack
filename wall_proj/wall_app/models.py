from django.db import models
import bcrypt
import re


class WallManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be at least 2 characters"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Enter a valid email address"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()
    # user_messages foreign key links messages to user in this class
    # user_comments foreign key links messages to user in this class

    # def __str__(self):
    #     return self.first_name + " " + self.last_name


class Message(models.Model):
    msg_content = models.CharField(max_length=255)
    posted_by = models.ForeignKey(
        User, related_name="user_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # message_comments foreign key links comments to message in this class
    objects = WallManager()


class Comment (models.Model):
    cmt_content = models.CharField(max_length=255)
    posted_by = models.ForeignKey(
        User, related_name="user_comments", on_delete=models.CASCADE)
    posted_to = models.ForeignKey(
        Message, related_name="message_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()
