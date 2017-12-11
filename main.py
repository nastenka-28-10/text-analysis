from datetime import datetime
from flask import Flask, render_template, request
import re


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Text analysis',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contacts'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Who is developer'
    )


@app.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.form.get('statistic', "") == "View statistics":
        task = "statistic"
        if request.files['file']:
            f = request.files['file']
            frequency = {}
            text_string = f.read().lower()
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string.decode('utf-8'))
            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1
            result_1 = []
            for w in sorted(frequency, key=frequency.get, reverse=True):
                result_1.append((w, frequency[w]))
            return render_template('statistic.html', result=result_1, task=task, upload_file=f)
        else:

            return "Upload your file please"

    elif request.form.get('wordlen', "") == "View words":
        task = "wordlen"
        if request.files['file']:
            f = request.files['file']
            frequency = {}
            text_string = f.read().lower()
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string.decode('utf-8'))
            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1
            sum = 0
            frequency_list = frequency.keys()
            length = request.form.get('num', '')
            result_2 = []
            for word in sorted(frequency_list):
                if str(len(word)) == length:
                    sum += frequency[word]
                    result_2.append(word)
            results = []
            results.append((result_2, sum))
            return render_template('wordlen.html', result=result_2, task=task, upload_file=f)
        else:
            return "Upload your file please"
if __name__ == '__main__':
  app.run(debug=True)