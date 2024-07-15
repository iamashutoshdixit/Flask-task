from flask import Flask, render_template, redirect, request,url_for
import database
import traceback


app = Flask(__name__)

db = database.Database(collection_name="note")

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('about.html')
    


@app.route('/contactus')
def contactus():
    return render_template('contact.html')


@app.route('/service')
def service():
    return render_template('service.html')




@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')
if __name__ == "__main__":
    app.run(debug=True)