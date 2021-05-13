
# Importing essential libraries
from flask import Flask, render_template, request
import requests
from google_trans_new import google_translator

translator = google_translator()

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('apple.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
            
    text_to_translate = translator.translate(message,'hi')
    text = text_to_translate
    return render_template('apple.html', prediction=text)    



if __name__ == '__main__':
	app.run(debug=True)
