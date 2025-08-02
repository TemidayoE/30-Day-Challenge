from django.db import models

class ToDo(models.Model):
  class Status(models.TextChoices):
    COMPLETE = "complete","Complete"
    INCOMPLETE = "incomplete","Incomplete"
  title = models.CharField(max_length=40)
  description = models.TextField(max_length=225,blank=True)
  status = models.CharField(max_length=10,choices=Status.choices,default=Status.INCOMPLETE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.title}:{self.Status}'