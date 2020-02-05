from django.db import models


# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=30)
    url = models.URLField()
    contents = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)  # 서버 시간을 읽어서 timestamp값을 만들어 추가

    def __str__(self):
        return "site name : " + self.site_name

    class Meta:
        ordering = ["-created"]