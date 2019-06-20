from django.db import models
from django.shortcuts import reverse

class Post(models.Model):                                                        # Класс для хранения данных постов в виде модели 
    title = models.CharField(max_length=150, db_index=True)                      # Заголовок поста. Максимальная длинна 150 символов. Включено индексирование (для удобства поиска)
    slug = models.SlugField(max_length=150, unique=True)                         # Слаг - человекопонятный URL. Может отсутствовать. Уникальный
    body = models.TextField(blank=True, db_index=True)                           # Тело поста. Может отсутствовать. Включено индексирование (для удобства поиска)
    tags = models.ManyToManyField("Tag", blank=True, related_name='posts')       # Тэг. Может быть пустой. 
    date_pub = models.DateTimeField(auto_now_add=True)                           # Дата публикации. Свойство auto_now_add - заполнение date_pub при сохранении в базу данных автоматически текущей датой



    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={"slug": self.slug})
    

    def __str__(self):                                                           # Переопределение метода STR(вывод информации об объекте)
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)


