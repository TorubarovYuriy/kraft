from django.contrib import admin
from .models import (
    Machine, Order, Roll, Clue, Work, Marriage, Box, WorkingShift, 
    MarriageCount,
)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')


class RollAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'weight', 'order'
    )
    list_editable = ('weight',)


class WorkingShiftAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'machine', 'plan', 'done',
    )
    list_editable = (
        'done',
    )
    empty_value_display = 'Не задано'
    filter_horizontal = ('users', 'rolls', 'work')


class MarriageCountAdmin(admin.ModelAdmin):
    list_display = (
        'working_shift', 'marriage', 'count_pieces', 'count_weight'
    )


admin.site.register(
    [Machine, Clue, Work, Marriage, Box]
)

admin.site.register(Order, OrderAdmin)
admin.site.register(Roll, RollAdmin)
admin.site.register(WorkingShift, WorkingShiftAdmin)
admin.site.register(MarriageCount, MarriageCountAdmin)
