from flask import Flask, render_template, url_for, flash, request
#import openxls
#os

app = Flask(__name__)
app.secret_key = 'LandingPage' #necessary for using flash messages

@app.route('/')
def home():
    #create request to retrive info from form
    #save info in an excel file
    #use os module to make sure xls file does not exist

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)