from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cointoss')
def coin_toss():
    title = "Coin Toss"
    return render_template('cointoss.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)