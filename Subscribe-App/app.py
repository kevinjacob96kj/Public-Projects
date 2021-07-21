from flask import Flask, request, render_template, redirect
from flask.helpers import send_file, url_for

app = Flask(__name__)
import sqlite3

####################################################################################

def get_EID_check(eid):
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    
    c.execute("select * from Login")
    conn.commit()
    
    data = c.fetchall()
    print(data)
    for item in data:
        print(item[0])
        if(item[0] == eid):
            print("True")
            return True
    print("False")
    return False

###################################################################################

@app.route('/')
def index():
    return render_template('index.html')

###################################################################################

@app.route('/', methods=['POST'])
def formPost():
    #Data from form
    eid = int(request.form['id'])
    fname = request.form['fname']
    lname = request.form['lname']

    #connect to database
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    #check if Employee ID exists.     
    check  = get_EID_check(eid)
    if(check):
        return redirect(url_for('exit', eid=eid))
    else:
        c.execute("INSERT INTO Login VALUES({}, '{}', '{}')".format(eid, fname, lname))
        conn.commit()
        return redirect(url_for('hello', fname=fname, lname=lname))


##################################################################################

@app.route('/<fname>/<lname>')
def hello(fname, lname):
    str = "Hello " + fname + " " +lname +". Welcome Back!!"
    return str


@app.route('/<eid>')
def exit(eid):
    str = eid + " already exists."
    return str

#################################################################################################################################################################

def fetchData():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    c.execute('SELECT * from Login')
    conn.commit()

    data = c.fetchall()
    return data

##################################################################################################

@app.route('/data')
def database():
    data = fetchData()
    return render_template('data.html', data=data)

##################################################################################################

@app.route('/deleteRecords')
def deleteRecords():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    c.execute("DELETE FROM Login")
    conn.commit()
    return render_template('data.html')

#################################################################################################################################################################

if __name__ == "__main__":
    app.run()    