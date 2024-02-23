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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def bootstrap(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Results</title>
                  </head>
                  <body>
                    <h1>Results of selection</h1>
                    <h3>The applicant for participation in the mission {nickname}</h3>
                    <div style="background-color: #76ff7a" class="alert alert-primary" role="alert">
                      <h4>Congratulations! Your rating after the {level} round</h4>
                    </div>
                    <h4>is {rating}</h4>
                    <div style="background-color: #f8f32b" class="alert alert-primary" role="alert">
                      <h4>Good luck!</h4>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(debug=True)