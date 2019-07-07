from django import template
from ..models import Post
from ..models import Post, Category

register = template.Library()

@register.assignment_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.assignment_tag
def archives():
    return Post.objects.datetimes('created_time', 'month', order='DESC')

@register.assignment_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()