from django.db import models


class UsersManager(models.Manager):
  def basic_validator(self, postData):
    errors={}
  
    if len(postData['name']) < 2:
      errors['name'] = 'El nombre de ususario debe tener al menos 4 letras'

    if len(postData['email']) < 4:
      errors['email'] = 'El email de ususario debe tener al menos 4 letras'
    
    if len(postData['password']) < 8:
      errors['password'] = 'La contraseña debe tener al menos 6 letras'
    
    if postData['password'] != postData['password_confirm']:
      errors['password'] = 'Las contraseñas no coinciden'
    
    return errors


class Users(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  allowed = models.BooleanField(default=True)
  avatar = models.URLField(default='https://i.pinimg.com/originals/13/f4/09/13f4093020fc96ba87eae8221d071af7.jpg')
  objects = UsersManager()