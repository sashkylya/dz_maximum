from django.db import models

class Advertisement(models.Model):
    title = models.CharField('Название', max_length=120)
    descriptions = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=9,decimal_places=2)
    trades = models.BooleanField('Торг',help_text='ЕСли хотим торговаться')
    date_now = models.DateField('Создание дата', auto_now_add= True)
    date_update = models.DateField('Обновление дата', auto_now= True)

    db_table = 'advertisements'

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
