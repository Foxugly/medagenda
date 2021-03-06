# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib import admin
from doctor.models import Doctor, ColorSlot, Invoice, TypePrice, InvoiceNumber


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    filter_horizontal = ['slots', 'invoices']


@admin.register(ColorSlot)
class ColorSlotAdmin(admin.ModelAdmin):
    pass


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceNumber)
class InvoiceNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(TypePrice)
class TypePriceAdmin(admin.ModelAdmin):
    pass
