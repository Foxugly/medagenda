# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from django.utils.dateformat import format
from django.utils import formats
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import os


class Address(Flowable):
    def __init__(self, up):
        Flowable.__init__(self)
        self.user = up.refer_userprofile.user
        self.adr = up.address
        self.x = 0
        self.y = 25
        self.width = 250
        self.height = 15
        self.styles = getSampleStyleSheet()

    def draw(self):
        p = Paragraph(u"%s %s" % (self.user.first_name, self.user.last_name), style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, self.width, self.height - self.y)
        p = Paragraph(u"%s %s" % (self.adr.route, self.adr.street_number), style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height - 15)
        p.drawOn(self.canv, self.width, self.height - 15 - self.y)
        p = Paragraph(u"%s %s" % (self.adr.locality.postal_code, self.adr.locality.name), style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height - 30)
        p.drawOn(self.canv, self.width, self.height - 30 - self.y)
        p = Paragraph(u"%s" % self.adr.locality.state.country, style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height - 45)
        p.drawOn(self.canv, self.width, self.height - 45 - self.y)


class PrintInvoice:
    def __init__(self, invoice, up):
        self.userprofile = up
        self.invoice = invoice
        self.elements = []
        # self.buffer = buffer
        # if pagesize == 'A4':
        self.pagesize = A4
        # elif pagesize == 'Letter':
        #    self.pagesize = letter
        self.width, self.height = self.pagesize
        self.styles = getSampleStyleSheet()

    def head(self):
        self.elements.append(Paragraph(u"%s" % settings.ENTREPRISE_NAME, self.styles['Normal']))
        self.elements.append(Paragraph(u"%s %s" % (settings.ENTREPRISE_FIRST_NAME, settings.ENTREPRISE_LAST_NAME),
                                       self.styles['Normal']))
        self.elements.append(Paragraph(u"%s" % settings.ENTREPRISE_ADDRESS, self.styles['Normal']))
        self.elements.append(
                Paragraph(u"%s %s" % (settings.ENTREPRISE_POSTAL_CODE, settings.ENTREPRISE_CITY),
                          self.styles['Normal']))
        self.elements.append(Paragraph(u"%s" % settings.ENTREPRISE_COUNTRY, self.styles['Normal']))
        self.elements.append(Paragraph(u"%s : %s" % (_(u"Mail"), settings.ENTREPRISE_EMAIL), self.styles['Normal']))
        self.elements.append(
                Paragraph(u"%s : %s" % (_(u"Phonenumber"), settings.ENTREPRISE_PHONENUMBER), self.styles['Normal']))
        self.elements.append(
                Paragraph(u"%s : %s" % (_(u"Entreprise number"), settings.ENTREPRISE_NUMBER), self.styles['Normal']))

    def save(self):
        path = os.path.join(settings.MEDIA_ROOT, self.invoice.path)
        doc = SimpleDocTemplate(path,
                                rightMargin=25 * mm,
                                leftMargin=25 * mm,
                                topMargin=30 * mm,
                                bottomMargin=25 * mm,
                                pagesize=self.pagesize)
        self.head()
        self.elements.append(Address(self.userprofile))
        self.elements.append(Spacer(0, 30 * mm))
        self.elements.append(Paragraph(u"%s" % _(u"Invoice"), self.styles['title']))
        self.elements.append(Spacer(0, 10 * mm))
        self.elements.append(
            Paragraph(u"%s : %010d" % (_(u"Invoice"), self.invoice.invoice_number), self.styles['Normal']))
        self.elements.append(Spacer(0, 5 * mm))
        date_format = formats.get_format('DATE_INPUT_FORMATS')[0]
        self.elements.append(
                Paragraph(u"Date : %s" % format(self.invoice.date_creation, date_format), self.styles['Normal']))
        self.elements.append(Spacer(0, 5 * mm))
        table_data = [[u"%s" % _(u"ID"), u"%s" % _(u"TYPE"), u"%s" % _(u"START DATE"), u"%s" % _(u"END DATE"),
                       u"%s" % _(u"PRIX TTC")],
                      [u"%s" % self.invoice.type_price.id, u"%s" % self.invoice.type_price, self.invoice.date_start,
                       self.invoice.date_end, u"%.2f euros " % self.invoice.price_incVAT]]
        cel_width = doc.width / 12
        user_table = Table(table_data,
                           colWidths=[cel_width, cel_width * 5, cel_width * 2, cel_width * 2, cel_width * 2])
        user_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
        self.elements.append(user_table)
        self.elements.append(Spacer(0, 10 * mm))
        self.elements.append(Paragraph(u"%s" % _(u"Thanks to pay the invoice in the month"), self.styles['Normal']))
        self.elements.append(Spacer(0, 10 * mm))
        self.elements.append(Paragraph(u"%s" % _(u"Banking details :"), self.styles['Normal']))
        self.elements.append(Paragraph(u"IBAN : %s" % settings.ENTREPRISE_IBAN, self.styles['Normal']))
        self.elements.append(Paragraph(u"BIC/SWIFT : %s" % settings.ENTREPRISE_BIC, self.styles['Normal']))
        mod = self.invoice.invoice_number % 97
        if mod == 0:
            mod = 97
        part2 = self.invoice.invoice_number % (10 ** 7)
        part1 = (self.invoice.invoice_number - part2) / (10 ** 7)
        part3 = (part2 % 1000)
        part2 = (part2 - part3) / 1000
        part3 = (part3 * 100) + mod
        self.elements.append(
                Paragraph("Structured communication : '+++%03d/%04d/%05d+++'" % (part1, part2, part3),
                          self.styles['Normal']))
        doc.build(self.elements)
