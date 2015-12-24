{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
    <div class="row row_space" >
        <div class="col-md-12 text-center"><h1>{%  trans "Offer" %}</h1></div>
    </div>
    <div class="row prices">
        <div class="col-sm-4 col-md-4">
            <div class="option">
                <div class="option-title">
                    <h3>Trial</h3>
                    <span>only for 2 months</span>
                </div>
                <div class="option-price">
                    <span class="price">€0</span>
                    <span class="period">per month</span>
                </div>
                <div class="option-list">
                    <ul class="item-list">
                        <li><strong>Customize your profile and data</strong></li>
                        <li><strong>Emails sent to patients with ical file</strong></li>
                        <li><strong>Add consultations to your calendar</strong></li>
                        <li><strong>No</strong> sms sent to patients</li>
                    </ul>
                    <button type="button" class="btn btn-success big"><i class="fa fa-hand-o-right hided-icon big"></i> Sign Up</button>
                </div>
            </div>
        </div>
        <div class="col-sm-4 col-md-4">
            <div class="option">
                <div class="option-title">
                    <h3>Standard</h3>
                    <span>most valued</span>
                </div>

                <div class="option-price">
                    <span class="price">€10</span>
                    <span class="period">per month</span>
                </div>

                <div class="option-list">
                    <ul class="item-list">
                        <li><strong>Customize your profile and data</strong></li>
                        <li><strong>Emails sent to patients with ical file</strong></li>
                        <li><strong>Add consultations to your calendar</strong></li>
                        <li><strong>No</strong> sms sent to patients</li>
                    </ul>
                    <button type="button" class="btn btn-success big"><i class="fa fa-hand-o-right hided-icon big"></i> Sign Up</button>
                </div>
            </div>
        </div>
        <div class="col-sm-4 col-md-4">
            <div class="option">
                <div class="option-title">
                    <h3>Premium</h3>
                    <span>extended version</span>
                </div>

                <div class="option-price">
                    <span class="price">€50</span>
                    <span class="period">per month</span>
                </div>

                <div class="option-list">
                    <ul class="item-list">
                        <li><strong>Customize your profile and data</strong></li>
                        <li><strong>Emails sent to patients with ical file</strong></li>
                        <li><strong>Add consultations to your calendar</strong></li>
                        <li><strong>Sms sent to patients</strong></li>
                    </ul>
                    <button type="button" class="btn btn-success big"><i class="fa fa-hand-o-right hided-icon big"></i> Sign Up</button>
                </div>
            </div>
        </div>
    </div>

{% endblock %}