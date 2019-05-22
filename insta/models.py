from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField()
    bio=HTMLField()
    name = models.CharField(max_length=255, null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email= models.EmailField(null=True)
    phonenumber = models.IntegerField(null=True)

    def __str__(self):
        return self.username

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name= models.CharField(max_length= 30)
    image_caption= models.CharField(max_length= 30)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True)
    # likes =
    # comments
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    
    @classmethod
    def display_images(cls):
        image = cls.objects.all()
        return image
    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image

