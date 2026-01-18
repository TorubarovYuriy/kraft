from datetime import time
from django.db import models
from django.contrib.auth import get_user_model


MAX_LENGTH_NAME: int = 255
DEFAULT_PLAN_DAY: int = 48000

USER = get_user_model()


class Machine(models.Model):
    """
    Docstring для Machine
        name - название машины
    Класс описывает машины на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Docstring для Order
        name - название заказа
        count - количество
        weight_one_piece - вес одной шт.
    Класс описывает заказы на производстве.
    """
    name = models.CharField('Имя', max_length=MAX_LENGTH_NAME)
    count = models.IntegerField('Количество')
    weight_one_piece = models.IntegerField(
        'вес одной шт. в граммах', null=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name


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

    class Meta:
        verbose_name = 'Рулон'
        verbose_name_plural = 'Рулоны'

    def __str__(self):
        return f'№ {self.number}. {self.order},  вес {self.weight}'


class Clue(models.Model):
    """
    Docstring для Clue
        name - название
        weight - вес
    Класс описывает клей который используется на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)
    weight = models.IntegerField('Вес')

    class Meta:
        verbose_name = 'Клей'
        verbose_name_plural = 'Клеи'

    def __str__(self):
        return self.name


class Work(models.Model):
    """
    Docstring для Work
        name - название
    Класс описывает виды работ на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name


class Marriage(models.Model):
    """
    Docstring для Marriage
        name - название
    Класс описывает виды брака на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    class Meta:
        verbose_name = 'Брак'
        verbose_name_plural = 'Браки'

    def __str__(self):
        return self.name


class Box(models.Model):
    """
    Docstring для Box
        name - название
    Класс описывает виды коробок на производстве.
    """
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)

    class Meta:
        verbose_name = 'Коробка'
        verbose_name_plural = 'Коробки'

    def __str__(self):
        return self.name


class MarriageCount(models.Model):
    """
    Docstring для MarriageCount
        marriage - вид брака
        working_shift - рабочая смена
        count_pieces - количество штук
        count_weight - количество гр.
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

    class Meta:
        verbose_name = 'Вид брака'
        verbose_name_plural = 'Виды брака'

    def __str__(self):
        return f'{self.marriage.name}'


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
    time_start = models.TimeField('Время начало смены', default=time(8, 0))
    time_end = models.TimeField('Время конца смены', default=time(17, 0))
    time_delta = models.IntegerField('Время смены', default=8)
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE, null=True, verbose_name='агрегат'
    )
    users = models.ManyToManyField(
        USER, verbose_name='Сотрудники', blank=True, default=None
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, verbose_name='заказ'
    )
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
    count_clue = models.IntegerField(
        'Количество клея кг.', null=True, blank=True
    )
    marriage = models.ManyToManyField(
        Marriage, verbose_name='Вид брака', through=MarriageCount
    )

    class Meta:
        verbose_name = 'Рабочая смена'
        verbose_name_plural = 'Рабочие смены'

    def __str__(self):
        return f'Смена от {self.date}.'
