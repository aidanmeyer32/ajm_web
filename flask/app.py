from flask import Flask, render_template
import os

app = Flask(__name__, 
    template_folder=os.path.join(os.path.dirname(__file__), '../html'),  # Set template folder
    static_folder=os.path.join(os.path.dirname(__file__), '../html'))  # Set static folder
    
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
