import os                                                                               #
import django                                                                           #   Магия подключения к базе данных Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogengine.settings")                  #                                                                                    # Django                                                                     #
django.setup()                                                                          #

#from django.db import models                                                               
from blog.models import Post, Tag                                                       #   Импорт моделей описанных в Django

model_python = Post(title='Post from Python4!', slug='Python4', body='Hello from python4!!!')
model_python.save()

print(dir(model_python))