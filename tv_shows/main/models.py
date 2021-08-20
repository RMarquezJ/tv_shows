from django.db import models


class showManager (models.Manager):
  def basic_validator(self, data):
    errors = {}
    if len(data['tit']) < 2:
      errors['title'] = 'The title must be longer than 2 characters'
    if len(data['net']) < 3:
      errors['network'] = 'The network name must be longer than 2 characters'
    if len(data['des']) <10:
      errors['description'] = 'The description must be longer than 10 characters'
    return errors

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
  objects = showManager()