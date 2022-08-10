from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=2048, blank=True, default='')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=6, blank=True, default='FFFFFF')
    hash = models.CharField(max_length=128)

    def __str__(self):
        return 'Post di ' + self.user.first_name + ' - ' + self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # On creation of the element calculate the hash of the title and store it in hash attribute
        # TODO: Fai attenzione nel calcolare l'hash, deve essere fatto solo sulla creazione e non a fronte di modifica
        pass

    def delete(self, using=None, keep_parents=False):
        # Make delete work
        # Codice
        super(BlogPost, self).delete(using=using, keep_parents=keep_parents)


class BlogPostComment(models.Model):
    blog_post = models.ForeignKey('prova.BlogPost', on_delete=models.PROTECT)
    text = models.CharField(max_length=2048)
    date_time = models.DateTimeField(auto_now=True)
