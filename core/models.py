from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/',blank=True, null=True )
    description = models.TextField(max_length=700)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(blank=True, null=False)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
