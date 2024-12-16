from flask import Flask, render_template, url_for, flash

app = Flask(__name__)
app.secret_key = 'LandingPage' #necessary for using flash messages

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)