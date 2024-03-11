from flask import Flask, render_template

# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров
# и отдельных товаров. Например,
# создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

app = Flask(__name__)


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)
@app.route('/data/')
def data():
    context = {'title': 'База статей.'}
    return render_template('data.html', **context)
