from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/noticia')
def noticia():
    return render_template('noticia.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/arearestrita/<status>')
def arearestrita(status):
    return render_template('arearestrita.html', status=status)

@app.route('/tema/<tema>')
def tema(tema):
    return render_template('tema.html', tema=tema)

@app.route('/galeria/<n>')
def galeria(n):
    return render_template('galeria.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)
