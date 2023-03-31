from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"       # 'always', 'hourly', 'daily', 'monthly', 'yearly', 'never'
    priority = 0.8

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on
