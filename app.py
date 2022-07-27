# Import from flask

from flask import Flask, render_template

# Flask constructor takes the name of current module (__name__)
app = Flask(__name__)

# Python decorator that Flask provides to assign URLs in our app
@app.route('/')
def landing_page():
    return "Hello World!"

@app.route('/app')
def example_page():
    return render_template('pages/index.html')


# Used to execute some code only if the file was run directly, and not imported
if __name__ == "__main__":
    app.run()