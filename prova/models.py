from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=2048, blank=True, default='')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=6, blank=True, default='FFFFFF')

    def __str__(self):
        return 'Post di ' + self.user.first_name + ' - ' + self.title
