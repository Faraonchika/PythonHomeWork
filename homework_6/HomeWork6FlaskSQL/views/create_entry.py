# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from wtforms import TextAreaField
from wtforms.validators import Length
import datetime
from HomeWork6FlaskSQL.storage import addto_db, getlast_key


def create_entry_page():
    error = ""
    params = TextAreaField('Текст статьи', validators=[Length(min=0, max=140)])
    if request.method == 'POST':
        title = request.form.get("name")
        text = request.form.get("article")
        created_at = (datetime.datetime.now()).strftime("%H:%M:%S - %b %d %Y")
        if title != "" and text != "":
            addto_db(title, text, created_at)
            key = getlast_key()
            return redirect(url_for('entry_page', key=key))
        else:
            error = "Введите, пожалуйста, все данные!"
    return render_template('create_entry.html', error=error)
