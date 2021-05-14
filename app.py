
# Importing essential libraries
from flask import Flask, render_template, request
import requests
from google_trans_new import google_translator  

translator = google_translator() 
#from googletrans import Translator

#translator = Translator()

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('apple.html')

@app.route('/predict', methods=['POST'])   
def predict():
	message = request.form['message']
	text_to_translate = translator.translate(message,lang_tgt='hi')
	#text1 = text_to_translate.text
	return render_template('apple.html', prediction=text_to_translate)

	


if __name__ == '__main__':
	app.run(debug=True)
