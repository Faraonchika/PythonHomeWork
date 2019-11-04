# -*- coding: utf-8 -*-
from flask import render_template, request
from HomeWork5.storage import BLOG_ENTRIES

def index_page():
    if request.method == 'POST':
        operation = request.form.get('operation')
        new = BLOG_ENTRIES
        if operation == "name":
            new.sort(key=lambda x: x['title'])
        elif operation == 'dateD':
            new.sort(key=lambda x: x['created_at'], reverse=True)
        elif operation == 'dateI':
            new.sort(key=lambda x: x['created_at'])
        return render_template('index.html', BLOG_ENTRIES=[x for x in new if request.form.get('name') in x["title"]])
    return render_template('index.html', BLOG_ENTRIES=BLOG_ENTRIES)
