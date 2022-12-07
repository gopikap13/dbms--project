from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/vehiclereg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config['MYSQL_HOST'] = 'localhost'
#MySQL username
app.config['MYSQL_USER'] = 'root'
#MySQL password here in my case password is null so i left empty
app.config['MYSQL_PASSWORD'] = ''
#Database name In my case database name is projectreporting
app.config['MYSQL_DB'] = 'vehiclereg'
#mysql = MySQL(app)
mysql = SQLAlchemy(app)

class Reg(mysql.Model):
    __tablename__ = 'reg'
    Sno = mysql.Column(mysql.Integer,primary_key=True)
    Year = mysql.Column(mysql.Integer, nullable=True)
    Model = mysql.Column(mysql.String(20), nullable=True)
    Color = mysql.Column(mysql.String(20), nullable=True)
    Mileage = mysql.Column(mysql.Integer, nullable=True)
    VIN = mysql.Column(mysql.Integer, nullable=True)
    Name = mysql.Column(mysql.String(20), nullable=True)
    Address = mysql.Column(mysql.String(20), nullable=True)
    City = mysql.Column(mysql.String(20), nullable=True)
    State = mysql.Column(mysql.String(20), nullable=True)
    Phone = mysql.Column(mysql.Integer, unique=True, nullable=True)
    Email = mysql.Column(mysql.String(20), unique=True, nullable=True)

@app.route('/')
def home():
    return render_template('details.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/user/reg', methods = ['POST'])
def reg():
    if(request.method=='POST'):
        year = request.form.get('year')
        model = request.form.get('model')
        color = request.form.get('color')
        mileage = request.form.get('mileage')
        vin = request.form.get('vin')
        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        phone = request.form.get('phone')
        email = request.form.get('email')
        entry = Reg(Year=year, Model=model, Color=color, Mileage=mileage, VIN=vin, Name=name, Address=address, City=city,State=state,Phone=phone, Email=email)
        mysql.session.add(entry)
        mysql.session.commit()
    allreg = Reg.query.all()
    return render_template('reg.html', allreg=allreg)

'''@app.route('/details', methods=['POST'])
def details():
    if request.method=='POST':
            year = request.args.get('year')
            model = request.args.get('model')
            color = request.args.get('color')
            mileage = request.args.get('mileage')
            vin = request.args.get('vin')
            name = request.args.get('name')
            address = request.args.get('address')
            city = request.args.get('city')
            state = request.args.get('state')
            phone = request.args.get('phone')
            email = request.args.get('email')
            entry = Reg(Year=year, Model=model, Color=color, Mileage=mileage, VIN=vin, Name=name, Address=address, City=city,State=state,Phone=phone, Email=email)
            mysql.session.add(entry)
            mysql.session.commit()
    allreg = Reg.query.all()
    return render_template('details.html',allreg=allreg)  '''



@app.route('/details')
def details():
    allreg = Reg.query.all()
    return render_template('details.html')

@app.route("/logout")
def logout():
    return redirect(url_for('home'))


@app.route('/show',methods=['GET','POST'])
def show():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from reg")
    data=cursor.fetchall()
    return render_template("show.html",data=data)
   
app.add_url_rule('/index','home',home)

if __name__ == '__main__':
    app.run(debug=True)