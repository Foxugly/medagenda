# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

# https://www.rossp.org/blog/easy-multi-part-e-mails-django/

from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site


def mail_collaborator(request, collaborator):
    subject_part = _('[medagenda] Subscription')
    template_name = 'mail/collaborator_subscription'
    context = {"collaborator": collaborator}
    msg = mail_body(request, subject_part, template_name, context)
    return msg.send()


def mail_patient_welcome(request, patient):
    subject_part = _('[medagenda] Confirm your email address')
    template_name = 'mail/patient_welcome'
    context = {"patient": patient}
    msg = mail_body(request, subject_part, template_name, context, patient.email)
    return msg.send()


def mail_user_welcome(request, userprofile, b_link):
    subject_part = _('[medagenda] Confirm your email address')
    template_name = 'mail/user_welcome'
    context = {"userprofile": userprofile, "b_link": b_link}
    msg = mail_body(request, subject_part, template_name, context, userprofile.user.email)
    return msg.send()


def mail_patient_new_appointment(request, slot):
    subject_part = _('[medagenda] New appointment')
    template_name = 'mail/patient_new_appointment'
    context = {"slot": slot}
    msg = mail_body(request, subject_part, template_name, context, slot.patient.email)
    msg.attach_file(slot.path)
    return msg.send()


def mail_patient_reminder(request, slot):
    # TODO faut complétement revoir
    subject_part = _('[medagenda] Reminder appointments')
    template_name = 'mail/patient_reminder'
    context = {"slot": slot}
    msg = mail_body(request, subject_part, template_name, context, slot.patient.email)
    return msg.send()


def mail_patient_cancel_appointment_from_doctor(request, slot):
    subject_part = _('[medagenda] Cancel appointment')
    template_name = 'mail/patient_cancel_appointment_from_doctor'
    context = {"slot": slot}
    msg = mail_body(request, subject_part, template_name, context, slot.patient.email)
    return msg.send()


def mail_patient_cancel_appointment_from_patient(request, slot, accepted):
    if accepted:
        subject_part = _('[medagenda] Cancel appointment accepted')
        template_name = 'mail/patient_cancel_appointment_from_patient_yes'
    else:
        subject_part = _('[medagenda] Cancel appointment refused')
        template_name = 'mail/patient_cancel_appointment_from_patient_no'
    context = {"slot": slot}
    msg = mail_body(request, subject_part, template_name, context, slot.patient.email)
    return msg.send()


def mail_body(request, subject_part, template_name, context, receiver):
    sender = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    context['site_name'] = current_site.name
    protocol = 'https' if request.is_secure() else 'http'
    context['uri'] = protocol + '://' + current_site.domain
    text_part = loader.get_template('%s.txt' % template_name).render(Context(context))
    html_part = loader.get_template('%s.tpl' % template_name).render(Context(context))
    msg = EmailMultiAlternatives(subject_part, text_part, sender, [receiver])
    msg.attach_alternative(html_part, "text/html")
    return msg
