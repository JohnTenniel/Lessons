from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] ='asaas5asd5asda4sdas2115a1sdasd6a5sdasd45a'

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Добавить курс', 'url': 'add_cource'},
    {'name': 'Информация', 'url': 'info'},
    {'name': 'Обратная связь', 'url': 'contact'},
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route('/add_cource')
def add_cource():
    return render_template('add_cource.html', title="Добавить Курс", menu=menu)

@app.route('/info')
def info():
    return render_template('info.html', title="Информация", menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category="success")
        else:
            flash("Ошибка отправки", category="error")
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', **context, title="Обратная связь", menu=menu)

    return render_template('contact.html', title="Обратная связь", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html', title="Страница не найдена", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
