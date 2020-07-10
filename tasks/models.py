from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    dateTime = models.DateTimeField(auto_now_add=True)

    def get_update_url(self):
        return reverse("tasks:task_update", kwargs={'id':self.id})
    
    def get_delete_url(self):
        return reverse("tasks:task_delete", kwargs={'id':self.id})
