from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://official-joke-api.appspot.com/jokes/random')
    
    if response.status_code == 200:
        joke = response.json()
        setup = joke.get('setup', 'No setup found.')
        punchline = joke.get('punchline', 'No punchline found.')
    else:
        setup = 'Oops! Could not fetch a joke.'
        punchline = 'Try refreshing the page.'

    return render_template('index.html', setup=setup, punchline=punchline)

if __name__ == '__main__':
    app.run(debug=True)