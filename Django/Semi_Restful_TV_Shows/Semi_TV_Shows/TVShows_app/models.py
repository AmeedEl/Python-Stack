from django.db import models
from datetime import datetime

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters."
            return errors
        
        existing_show = Show.objects.filter(title=postData['title']).exclude(id=postData.get('id'))
        if existing_show.exists():
            errors["title"] = "A show with this title already exists."
            return errors
        
        if len(postData['network']) < 3:
            errors["desc"] = "Network name should be at least 3 characters."
            return errors
        
        if not postData.get('released_date'):
            errors["released_date"] = "Release date is required."
            return errors
        
        if len(postData['desc']) > 1 and len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters."
            return errors
        
        released_date = datetime.strptime(postData['released_date'], "%Y-%m-%d").date()
        if released_date > datetime.today().date():
            errors["released_date"] = "Release date cannot be in the future."
            return errors
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    released_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
    