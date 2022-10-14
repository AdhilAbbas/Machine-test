from turtle import width
from django.db import models
from PIL import Image

# Create your models here.
class Upload(models.Model):
    picture = models.ImageField(null=True,upload_to='media/')

    def save(self, *args, **kwargs):

        super(Upload, self).save(*args, **kwargs)
        if self.picture: 
            print("============ image found ===============")
            im = Image.open(self.picture.path)
            width, height = im.size
            left = 5
            top = height / 4
            right = 164
            bottom = 3 * height / 4
            im1 = im.crop((left,top,right,bottom))
            im1.save(self.picture.path)
    