# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from datetime import date
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from django.utils.dateformat import format
from django.utils import formats
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Address(Flowable):
    def __init__(self, x=0, y=25, width=250, height=15):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.styles = getSampleStyleSheet()

    def draw(self):
        p = Paragraph("Prenom_client Nom_client", style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, self.width, self.height - self.y)
        p = Paragraph("Adresse1", style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height-15)
        p.drawOn(self.canv, self.width, self.height-15 - self.y)
        p = Paragraph("Adresse2", style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height-30)
        p.drawOn(self.canv, self.width, self.height-30 - self.y)
        p = Paragraph("PAYS", style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height-45)
        p.drawOn(self.canv, self.width, self.height-45 - self.y)


class Invoice:
    def __init__(self, buffer, pagesize):
        self.elements = []
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize
        self.styles = getSampleStyleSheet()
           
    def head(self):
        self.elements.append(Paragraph(u"%s" % settings.entreprise_name, self.styles['Normal']))
        self.elements.append(Paragraph(u"%s %s" % (settings.entreprise_first_name, settings.entreprise_last_name), self.styles['Normal']))
        self.elements.append(Paragraph(u"%s" % settings.entreprise_address, self.styles['Normal']))
        self.elements.append(Paragraph(u"%s %s" % (settings.entreprise.postal_code, settings.city), self.styles['Normal']))
        self.elements.append(Paragraph(u"%s" % settings.country, self.styles['Normal']))
        self.elements.append(Paragraph(u"%s : %s" % (_(u"Mail"), settings.entreprise_email), self.styles['Normal']))
        self.elements.append(Paragraph(u"%s : %s" % (_(u"Phonenumber"), settings.entreprise_phone), self.styles['Normal']))
        self.elements.append(Paragraph(u"%s : %s" % (_(u"Entreprise number"), settings.entreprise_number), self.styles['Normal']))

    def print_users(self):
        doc = SimpleDocTemplate(self.buffer,
                                rightMargin=25*mm,
                                leftMargin=25*mm,
                                topMargin=30*mm,
                                bottomMargin=25*mm,
                                pagesize=self.pagesize)
        self.head()
        self.elements.append(Address())
        self.elements.append(Spacer(0, 30*mm))
        self.elements.append(Paragraph("Invoice", self.styles['title']))
        self.elements.append(Paragraph("Facture : ", self.styles['Normal']))
        date_format = formats.get_format('DATE_FORMAT')
        self.elements.append(Paragraph("Date : %s" % format(date.today(), date_format), self.styles['Normal']))
        self.elements.append(Spacer(0, 10*mm))
        table_data = [["ID", "TYPE", "START DATE", "END DATE", "PRIX TTC"]]
        #table_data.append(["alpha2", "beta2", "delta2", "gamma2", "omega2"])
        cel_width = doc.width/12
        user_table = Table(table_data, colWidths=[cel_width, cel_width*5, cel_width*2, cel_width*2, cel_width*2])
        user_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
        self.elements.append(user_table)
        self.elements.append(Spacer(0, 10*mm))
        self.elements.append(Paragraph("Thanks to pay the invoice in the month", self.styles['Normal']))
        self.elements.append(Spacer(0, 10*mm))
        self.elements.append(Paragraph("Banking details :", self.styles['Normal']))
        self.elements.append(Paragraph("IBAN : BE123456789", self.styles['Normal']))
        self.elements.append(Paragraph("BIC : DEUT123456", self.styles['Normal']))
        doc.build(self.elements)
 
        #pdf = buffer.getvalue()
        #buffer.close()
        #return pdf
        
i = Invoice("invoice.pdf", "A4")
i.print_users()
