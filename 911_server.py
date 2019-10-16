
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogengine.settings")

import django
django.setup()

from django.db import models

#class Post(models.Model):                                                        # Класс для хранения данных постов в виде модели 
#    title = models.CharField(max_length=150, db_index=True)                      # Заголовок поста. Максимальная длинна 150 символов. Включено индексирование (для удобства поиска)
#    slug = models.SlugField(max_length=150, blank=True, unique=True)                         # Слаг - человекопонятный URL. Может отсутствовать. Уникальный
#    body = models.TextField(blank=True, db_index=True)                           # Тело поста. Может отсутствовать. Включено индексирование (для удобства поиска)
#    tags = models.ManyToManyField("Tag", blank=True, related_name='posts')       # Тэг. Может быть пустой. 
#    date_pub = models.DateTimeField(auto_now_add=True)                           # Дата публикации. Свойство auto_now_add - заполнение date_pub при сохранении в базу данных автоматически текущей датой



































message_from_FM = '$1501.20190125102355;T;356895031151098;897010210542721818,1,25002;S,10020312483,01FF,1700;P,”161229.487,3723.2475,N,12158.3416,E,1.10,0.43,73.75”;C,”262,01,3008,6060,66,262,01,3008,DDD1,80,262,01,008,BFBE,86,262,01,3008,BB44,89,262,01,3008,8307,93”;*5F\r\n'



def validation(message):
    message_crc = message.split(';')[-1:]
    print(message_crc)
    message_bytes = bytes(message, 'utf-8')
    crc = 0
    for symbol in message_bytes:
        crc = crc + symbol
    crc = str(hex(crc % 256))[2:].upper()

    
    print(crc)
    #print()
    #print(message_crc)
    
validation(message_from_FM)


def createMessage():
    # Создание CRC для сообщения

    message = b'$1501.20180910094609;X;866796036836845;89701012417811708675,1,25001;S,0234,0700,+23,1;C,"250,01,00DD,3860,66,250,20,4D0E,14E8,66,250,02,1285,2C3A,67,250,02,1285,2C39,69,250,02,1285,2C3D,70,250,99,39A5,2E60,71";Q,1,82,0;N,[M2,S60,P15,p25,N30,t-30,G60,g2,F12];L,r10,7,t7,p4,0,s0,0,m360,0,10,0,o0,c211,85,g1,m0,a0,d0,0,n154,0,F0:0,0,5,27:0,4,55,50:rn;'
    crc = 0
    for symbol in message:
        crc = crc + symbol
    crc = crc % 256
    return message + b'*' + bytes(str(hex(crc))[2:].upper(), 'utf-8') + b'\r\n'