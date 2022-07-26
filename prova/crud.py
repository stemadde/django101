from prova.models import BlogPost


def get_blog_posts(user):
    return BlogPost.objects.filter(user=user)
