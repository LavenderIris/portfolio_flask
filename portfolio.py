from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_portfolio():
    return render_template('main.html')    # Render the template and return it!

@app.route('/projects')
def projects():
    return render_template('projects.html')  

@app.route('/about')
def about():
    return render_template('about.html')  

app.run(debug=True)