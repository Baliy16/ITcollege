from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Ваш код програми, який ви хочете вивести на веб-сторінці
    output = "Привіт, це мій перший веб-сайт з використанням Flask!"
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
