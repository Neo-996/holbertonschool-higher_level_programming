from flask import Flask, render_template

app = Flask(__name__)

# Home route renders index.html
@app.route('/index')
def home():
    return render_template('index.html')

# About page route renders about.html
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page route renders contact.html
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Run app on port 5000 with debug mode on
    app.run(debug=True, port=5000)
