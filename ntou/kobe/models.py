from django.db import models
from django.conf import settings

class KobePost(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(blank = True, max_length = 100, verbose_name = '暱稱（選填）')
    content = models.TextField(verbose_name = '發文內容')
    photo = models.ImageField(blank=True, upload_to = 'photos/' , verbose_name = '上傳照片')
    postTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)
