from django.contrib import admin
from .models import (
    Machine, Order, Roll, Clue, Work, Marriage, Box, WorkingShift
)


admin.site.register(
    [Machine, Order, Roll, Clue, Work, Marriage, Box, WorkingShift]
)
