from django.db import models
from django.contrib.auth import get_user_model


MAX_LENGTH_NAME = 255
DEFAULT_PLAN_DAY = 48000

USER = get_user_model()

class Machine(models.Model):
    """
    Docstring для Machine
        name - название машины
    Класс описывает машины на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

class Order(models.Model):
    """
    Docstring для Order
        name - название заказа
        count - количество
    Класс описывает заказы на производстве.
    """
    name = models.CharField('Имя', max_length=MAX_LENGTH_NAME)
    count = models.IntegerField('Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Roll(models.Model):
    """
    Docstring для Roll
        order - заказ
        weight - вес
        number - номер
    Класс описывает рулоны которые используются при работе.
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, verbose_name='заказ'
    )
    weight = models.IntegerField('Вес')
    number = models.IntegerField('Номер')

    def __str__(self):
        return self.order.name

    class Meta:
        verbose_name = 'Рулон'
        verbose_name_plural = 'Рулоны'


class Clue(models.Model):
    """
    Docstring для Clue
        name - название
        weight - вес
    Класс описывает клей который используется на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)
    weight = models.IntegerField('Вес')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Клей'
        verbose_name_plural = 'Клеи'


class Work(models.Model):
    """
    Docstring для Work
        name - название
    Класс описывает виды работ на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Marriage(models.Model):
    """
    Docstring для Marriage
        name - название
    Класс описывает виды брака на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брак'
        verbose_name_plural = 'Браки'


class Box(models.Model):
    """
    Docstring для Box
        name - название
    Класс описывает виды коробок на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коробка'
        verbose_name_plural = 'Коробки'


class MarriageCount(models.Model):
    """
    Docstring для MarriageCount
        marriage - вид брака
        count - количество
        working_shift - рабочая смена
    Класс описывает виды брака на производстве.
    """
    marriage = models.ForeignKey(
        Marriage, on_delete=models.CASCADE, verbose_name='брак'
    )
    working_shift = models.ForeignKey(
        'WorkingShift', on_delete=models.CASCADE, verbose_name='рабочая смена'
    )
    count_pieces = models.IntegerField('Количество в шт')
    count_weight = models.IntegerField('Количество в гр.')

    def __str__(self):
        return f'{self.marriage.name} {self.count}'
    
    class Meta:
        verbose_name = 'Вид брака'
        verbose_name_plural = 'Виды брака'


class WorkingShift(models.Model):
    """
    Docstring для WorkingShift
        date - дата
        time_start - время начала смены
        time_end - время конца смены
        time_delta - время смены
        machine - агрегат
        users - сотрудники
        order - заказ
        work - работы
        plan - план
        done - выполнено
        rolls - рулоны
        box - коробка
        count_box - количество коробок
        clue - клей
        count_clue - количество клея
        marriage - вид брака
    Класс описывает рабочую смену на производстве.
    """
    date = models.DateField('Дата')
    time_start = models.TimeField('Время начало смены')
    time_end = models.TimeField('Время конца смены')
    time_delta = models.IntegerField('Время смены')
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE, null=True, verbose_name='агрегат'
    )
    users = models.ManyToManyField(
        USER, verbose_name='Сотрудники', blank=True, default=None
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    work = models.ManyToManyField(Work, verbose_name='Работы')
    plan = models.IntegerField('План', null=True, default=DEFAULT_PLAN_DAY)
    done = models.IntegerField('Выполнено', null=True)
    rolls = models.ManyToManyField(Roll, verbose_name='Рулоны')
    box = models.ForeignKey(
        Box, on_delete=models.CASCADE, verbose_name='Коробка'
    )
    count_box = models.IntegerField('Количество коробок', null=True)
    clue = models.ForeignKey(
        Clue, on_delete=models.CASCADE, verbose_name='Клей',
        blank=True, null=True, default=None,
    )
    count_clue = models.IntegerField('Количество клея кг.', null=True)
    marriage = models.ManyToManyField(
        Marriage, verbose_name='Вид брака', through=MarriageCount
    )

    def __str__(self):
        return f'Смена от {self.date}.'
    
    class Meta:
        verbose_name = 'Рабочая смена'
        verbose_name_plural = 'Рабочие смены'