from django.db import models


class Networks(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Shows(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  rel_date = models.DateTimeField()
  network = models.ForeignKey(Networks, related_name="show", on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)