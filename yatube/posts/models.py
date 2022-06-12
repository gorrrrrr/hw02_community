from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Название", max_length=200,)
    address = models.URLField(blank=True, null=True, max_length=200,)
    slug = models.SlugField("Текст для ссылки", unique=True)
    description = models.TextField("Описание",)

    def __str__(self):
        return f'Группа - {self.title}'


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name="Автор",
                               )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Группа",
    )

    def __str__(self):
        return self.text
