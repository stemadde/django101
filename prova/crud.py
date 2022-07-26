from typing import Optional

from django.contrib.auth.models import User
from django.db.models import QuerySet
from prova.models import BlogPost


def get_blog_posts(user: User) -> QuerySet:
    return BlogPost.objects.filter(user=user)


def create_blog_post(title: str, text: str, user: User, color: str) -> BlogPost:
    pass


def delete_blog_post(post_id: int) -> int:
    """
    :param post_id:
    :return: Status code -> 200 = ok, 500 = error
    """
    pass


def updated_blog_post(post_id: int, **kwargs) -> Optional[BlogPost]:
    pass
