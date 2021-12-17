import django_filters
from .models import Blog


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['title']
