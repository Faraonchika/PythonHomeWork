# -*- coding: utf-8 -*-
from flask import render_template, request
from HomeWork5.storage import BLOG_ENTRIES


def entry_page(key):
    article = [x for x in BLOG_ENTRIES if x['key'] == key]
    length = len(article)
    error1 = ""
    if request.method == 'POST':
        name =  request.form.get("name")
        text = request.form.get("text")
        if name != "" or text != "":
            next(item['comments'].append({"name": name, "text": text}) for item in BLOG_ENTRIES if item["key"] == key)
        else:
            error1 = "Введите данные для коментария!"
    return render_template('entry.html', article=article[0], length=length, error1=error1)
