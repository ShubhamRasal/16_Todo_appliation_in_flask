from flask import Flask,request, redirect, render_template,url_for
from functions.models import ToDoModel

app = Flask(__name__)


@app.route('/hey') 
def hello():
    return "<h1><b>Hello</b></h1>"

@app.route('/') #this is when user hits url
def sql_database():
   
    results=ToDoModel().list_items()
    #print('results',results)
    return render_template('todo.html',results=results)


@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def insert():
    if request.method == 'POST':
       title=request.form['Title']
       des=request.form['Description']
       Date=request.form['DueDate']
       ToDoModel().sql_edit_insert((title,des,Date))
       return redirect(url_for('sql_database'))
       #return "<h1> Hey in insert</h1>"

@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def delete():
    print("Inside delete")
    if request.method == 'GET':
        ID = request.args.get('ID')
        #print("lname",ID)
        ToDoModel().sql_delete((ID,))
        return redirect(url_for('sql_database'))

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def editlink():
    if request.method == 'GET':
        ID=request.args.get('ID')
        where=' and id='+ID
        eresults=ToDoModel().list_items(where)
        results=ToDoModel().list_items()
        #print('eresults',eresults)
        return render_template('todo.html',eresults=eresults,results=results)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def edit():
    old_id=request.form['old_ID']
    title=request.form['Title']
    des=request.form['Description']
    date=request.form['DueDate']    
    ToDoModel().sql_edit((title,des,date,old_id))
    return redirect(url_for('sql_database'))

if __name__ == "__main__":
    app.run(debug=True)
