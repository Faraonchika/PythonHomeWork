from flask import render_template, redirect
from MainSite.storage import ARTICLES
from MainSite.static.articles.numbers import d


def watch_page(value, key):
    if int(key) < 5:
        with open('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/articles/data_handling/' + value + '.txt', 'r', encoding="utf-8") as file:
            lib = file.readlines()
        return redirect(lib[0])

    elif 5 <= int(key) < 15:
        with open('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/articles/supervised_learning/' + value + '.txt', 'r', encoding="utf-8") as file:
            lib = file.readlines()
        return redirect(lib[0])

    elif 15 <= int(key) < 30:
        with open('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/articles/unsupervised_learning/' + value + '.txt', 'r', encoding="utf-8") as file:
            lib = file.readlines()
            return redirect(lib[0])
    # return render_template('watch.html', lib=lib, value=value)

