# -*- coding: utf-8 -*-
from flask import render_template, request
from HomeWork6FlaskSQL.storage import read_db, add_comment


def entry_page(key):
    if request.method == 'POST':
        name = request.form.get("name")
        text = request.form.get("text")
        if name != "" or text != "":
            add_comment(key, name, text)
        else:
            error1 = "Введите данные для коментария!"
    article = [x for x in read_db() if str(x['key']) == key]
    length = len(article)
    error1 = ""
    return render_template('entry.html', article=article[0], length=length, error1=error1)
