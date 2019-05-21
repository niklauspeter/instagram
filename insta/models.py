from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name= models.CharField(max_length= 30)
    image_caption= models.CharField(max_length= 30)
    # profile = models.ForeignKey(Profile)
    # likes =
    # comments
    pub_date = models.DateTimeField(auto_now_add=True)