from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    student_id = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    def __str__(self):
        return self.title
