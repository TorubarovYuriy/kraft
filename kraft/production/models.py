from django.db import models
from django.contrib.auth import get_user_model


MAX_LENGTH_NAME = 255

USER = get_user_model()

class Machine(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

class Order(models.Model):
    name = models.CharField('Имя', max_length=MAX_LENGTH_NAME)
    count = models.IntegerField('Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Roll(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    weight = models.IntegerField('Вес')
    number = models.IntegerField('Номер')

    def __str__(self):
        return self.order.name

    class Meta:
        verbose_name = 'Рулон'
        verbose_name_plural = 'Рулоны'


class Clue(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)
    weight = models.IntegerField('Вес')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Клей'
        verbose_name_plural = 'Клеи'


class Work(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Marriage(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брак'
        verbose_name_plural = 'Браки'


class Box(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коробка'
        verbose_name_plural = 'Коробки'


class WorkingShift(models.Model):
    date = models.DateField('Дата')
    time_start = models.TimeField('Время начало')
    time_end = models.TimeField('Время конца')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(USER)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
    plan = models.IntegerField('План', null=True)
    done = models.IntegerField('Выполнено', null=True)
    rolls = models.ManyToManyField(Roll)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    count_box = models.IntegerField('Количество коробок', null=True)
    clue = models.ForeignKey(Clue, on_delete=models.CASCADE)
    count_clue = models.IntegerField('Количество клея кг.', null=True)
    marriage = models.ForeignKey(Marriage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Смена от {self.date}.'
    
    class Meta:
        verbose_name = 'Рабочая смена'
        verbose_name_plural = 'Рабочие смены'