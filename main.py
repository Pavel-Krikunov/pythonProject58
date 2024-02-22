from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt='The photo of Mars'>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promote():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Promotion</title>
                  </head>
                  <body>
                    <p>Человечество вырастает из детства.</p><br>
                    <h1>Человечеству мала одна планета.</h1><br>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1><br>
                    <h1>И начнем с Марса!</h1><br>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/bootstrap_sample')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                    <h1 style="color: red">Wait for us, Mars!</h1>
                  </head>
                  <body>
                  <img src="{url_for('static', filename='img/mars.jpg')}" alt='The photo of Mars'>
                    <div style="background-color: #c0c0c0" class="alert alert-primary" role="alert">
                      Humanity growth from childhood.
                    </div>
                    <div style="background-color: #47a76a" class="alert alert-primary" role="alert">
                      One planet is small for us.
                    </div>
                    <div style="background-color: #c0c0c0" class="alert alert-primary" role="alert">
                      We will make still lifeless planets inhabited.
                    </div>
                    <div style="background-color: #fbec5d" class="alert alert-primary" role="alert">
                      And we will begin from Mars.
                    </div>
                    <div style="background-color: #fadbc8" class="alert alert-primary" role="alert">
                      Join us!!!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
