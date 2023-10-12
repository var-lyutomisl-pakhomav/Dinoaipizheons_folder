from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('illustrate.html')

if __name__ == '__main__':
    import webbrowser
    webbrowser.open('http://localhost:5000/')
    app.run()

