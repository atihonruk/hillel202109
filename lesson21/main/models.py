import random

from django.conf import settings
from django.db import models
from django.utils.baseconv import base56

# 012345679abcdef
# base64 A-Za-z
# base56

MIN_KEY, MAX_KEY = 80106440, 550731755


def gen_key():
    return base56.encode(random.randint(MIN_KEY, MAX_KEY))


class Url(models.Model):
    url = models.URLField()
    key = models.SlugField()
    user = settings.AUTH_USER_MODEL

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key = gen_key()
            
        super().save(*args, **kwargs)
