from flask import Flask, render_template, redirect, request
import database
import traceback


app = Flask(__name__)

db = database.Database(collection_name="note")


@app.route("/")
def index():
    try:
        all_data =[i for i in db.get_all()]
        return render_template('index.html', data = all_data, data_len = len(all_data))
    
    except Exception as err:
        traceback.print_exc()
        return {"detail":str(err)}, 403



@app.route("/search/", methods=['POST'])
def search_note():
    try:
        search_text = request.form.get('search')
        all_data =[i for i in db.search_content(search_text)]
       

        return render_template('index.html', data = all_data, data_len = len(all_data))
    
    except Exception as err:
        traceback.print_exc()
        return {"detail":str(err)}, 403


@app.route("/add", methods=['POST'])
def add_note():
    try:
        content = request.form.get('content')
        db.insert_content(content)

        return redirect('/')
    
    except Exception as err:
        traceback.print_exc()
        return {"detail":str(err)}, 403

@app.route('/delete/<note_id>')
def delete_note(note_id):
    try:

        db.delete_content(note_id)
        return redirect('/')
    
    except Exception as err:
        traceback.print_exc()
        return {"detail":str(err)}, 403

@app.route('/update/<note_id>', methods=['POST'])
def update_note(note_id):
    try:
        new_content = request.form.get('content')
        db.edit_content(note_id=note_id,new_content=new_content)
        return redirect('/')
    
    except Exception as err:
        traceback.print_exc()
        return {"detail":str(err)}, 403


if __name__ == "__main__":
    app.run(debug=True)