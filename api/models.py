from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    complited = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.task
    

    def to_dict(self):
        returned = {
            'id':self.id,
            'task':self.task,
            'description':self.description,
            'complited':self.complited

        }
        return returned
