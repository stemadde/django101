from typing import Optional
from django.contrib.auth.models import User
from django.db.models import QuerySet
from prova.models import BlogPost


def get_blog_posts(user: User) -> QuerySet:
    return BlogPost.objects.filter(user=user)


def get_blog_post(user:User, post_id: int) -> Optional[BlogPost]:
    return get_blog_posts(user).filter(id=post_id).first()


def create_blog_post(title: str, text: str, user: User, color: str) -> BlogPost:
    return BlogPost.objects.create(title=title, text=text, user=user, color=color)


def delete_blog_post(user: User, post_id: int) -> int:
    """
    :param user: User object
    :param post_id:
    :return: Status code -> 204 = ok, 404 = error
    """
    # ugly except but meh, don't know what .delete() throws
    try:
        BlogPost.objects.filter(user=user, id=post_id).first().delete()
        return 204
    except AttributeError:
        return 404


def updated_blog_post(user: User, post_id: int, **kwargs) -> Optional[BlogPost]:
    bp = BlogPost.objects.filter(user=user, id=post_id).first()
    if bp:
        bp.save(**kwargs)
        return bp

#ALL IS TO BE TESTED
