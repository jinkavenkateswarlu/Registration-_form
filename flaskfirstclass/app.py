from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
app=Flask(__name__)
mydb=mysql.connector.connect(host='localhost',user='root',password='Venkey@2003',db='codegnan')
with mysql.connector.connect(host='localhost',user='root',password='Venkey@2003',db='codegnan'):
    cursor=mydb.cursor(buffered=True)
    cursor.execute("create table if not exists form(name varchar(50),email varchar(150),message text)")
    cursor.execute("create table if not exists Regform(firstname varchar(50),middlename varchar(150),lastname text,day text,month text, year text,street varchar(50),village varchar(50),mondal varchar(50),district varchar(50),state varchar(50),Email varchar(50),Phone text)")
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into form values(%s,%s,%s)',[name,email,message])
        mydb.commit()
        cursor.close()
    return render_template('login.html')
@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        middlename = request.form.get('middlename')
        lastname = request.form.get('lastname')
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')
        street = request.form.get('street')
        village = request.form.get('village')
        mondal = request.form.get('mondal')
        district = request.form.get('district')
        state = request.form.get('state')
        email = request.form.get('email')
        phone = request.form.get('phone')
        cursor = mydb.cursor(buffered=True)
        cursor.execute('INSERT INTO Regform (firstname, middlename, lastname, day, month, year, street, village, mondal, district, state, email, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       [firstname, middlename, lastname, day, month, year, street, village, mondal, district, state, email, phone])
        mydb.commit()
        cursor.close()
        return redirect(url_for('login'))
    
    return render_template('regestrationform.html')
@app.route('/radio',methods=['GET','POST'])
def radio():
    return render_template('radiobuttons.html')
app.run(debug=True,use_reloader=True)