# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from wtforms import TextAreaField
from wtforms.validators import Length
from HomeWork5.storage import BLOG_ENTRIES
import datetime


def create_entry_page():
    error = ""
    params = TextAreaField('Текст статьи', validators=[Length(min=0, max=140)])
    if request.method == 'POST':
        key = str(len(BLOG_ENTRIES) + 1)
        title = request.form.get("name")
        text = request.form.get("article")
        created_at = datetime.datetime.now()
        if title != "" and text != "":
            BLOG_ENTRIES.append({
            'key': key,
            'title': title,
            'text': text,
            'created_at': created_at,
            'comments': [
            ]
             })
            return redirect(url_for('entry_page', key=key))
        else:
            error = "Введите, пожалуйста, все данные!"
    return render_template('create_entry.html', error=error)
