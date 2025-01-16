from django.db import models

class Certificate(models.Model):
    Статус_регистрации = models.CharField(max_length=255)
    Регистрационный_талон = models.CharField(max_length=255)
    Регистрация = models.CharField(max_length=100)
    Регистрация_по = models.CharField(max_length=150)
    Номер_паспорта = models.CharField(max_length=150)
    Страна_паспорта = models.CharField(max_length=150)
    Фамилия = models.CharField(max_length=300)
    Имя = models.CharField(max_length=300)
    Отчество = models.CharField(max_length=300)
    Дата_рождения = models.CharField(max_length=300)
    Адрес_проживания = models.CharField(max_length=300)
    
    