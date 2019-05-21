from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField()
    bio=models.CharField(max_length=150)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name= models.CharField(max_length= 30)
    image_caption= models.CharField(max_length= 30)
    # profile = models.ForeignKey(Profile)
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

