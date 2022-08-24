from django.db import models
import hashlib

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=2048, blank=True, default='')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=6, blank=True, default='FFFFFF')
    hash = models.CharField(max_length=128, default=None)

    def __str__(self):
        return 'Post di ' + self.user.first_name + ' - ' + self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # On creation of the element calculate the hash of the title and store it in hash attribute
        # TODO: Fai attenzione nel calcolare l'hash, deve essere fatto solo sulla creazione e non a fronte di modifica
        # Should work, gonna test later
        if self.hash is None:
            self.hash = hashlib.md5(bytes(self.title, encoding='utf-8')).hexdigest()
        super(BlogPost, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        # Make delete work  ok :) -Daniele
        # .all() is redudant, but at least i'm 100% i'm working on a qset and not on some weird object
        BlogPostComment.objects.filter(blog_post=self.pk).all().delete()
        super(BlogPost, self).delete(using, keep_parents)


class BlogPostComment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    blog_post = models.ForeignKey('prova.BlogPost', on_delete=models.PROTECT)
    subtitle = models.CharField(max_length=256)
    text = models.CharField(max_length=2048)
    date_time = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(BlogPostComment, self).save(force_insert, force_update, using, update_fields)
        return self