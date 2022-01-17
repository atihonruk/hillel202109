from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

# 2. Основная сущность - Post с такими обязательными атрибутами:
# title (заголовок)
# text (тело поста)
# slug
# created_by (ссылка на автора)
# created_at (дата/время создания)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField()
    created_by = settings.AUTH_USER_MODEL
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload/%Y/%m/%d')

    # image.url
    
    def __str__(self):
        return f'Post {self.id}: {self.title}'

    def get_absolute_url(self):
        return reverse('posts', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.pk: # id
            # unidecode
            slug = slugify(self.title) # 'My First post' -> '123-my-first-post'
            self.slug = slug
        super().save(*args, **kwargs)




# Писать посты могут только аутентифицированные пользователи. Slug сгенерируйте автоматически, из title например (подсказка, django.utils.test.slugify).

