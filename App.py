import flask
import sqlalchemy.orm
from models import Employee


app = flask.Flask(__name__)
app.secret_key = "Secret Key"

"""
Create an engine of connections, which the Session
will use for connection resources.
"""
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@localhost/crud', echo=False,
                                  connect_args={'auth_plugin': 'mysql_native_password'})
"""
Create a configured Session class.
"""
Session = sqlalchemy.orm.sessionmaker(bind=engine)
"""
Create a session.
"""
session = Session()


# Landing page of the Application
# Read function
@app.route('/')
def index():
    all_employees = session.query(Employee).all()
    return flask.render_template('index.html', employees=all_employees)


# Insert function
@app.route('/insert', methods=['POST'])
def insert():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        email = flask.request.form['email']
        phone = flask.request.form['phone']

        employee = Employee(name, email, phone)
        session.add(employee)
        session.commit()
        flask.flash("Employee inserted successfully!")

        return flask.redirect(flask.url_for('index'))


# Update function
@app.route('/update', methods=['GET', 'POST'])
def update():
    if flask.request.method == 'POST':
        employee = session.query(Employee).filter_by(id=(flask.request.form.get('id'))).first()

        employee.name = flask.request.form['name']
        employee.email = flask.request.form['email']
        employee.phone = flask.request.form['phone']

        session.commit()
        flask.flash("Employee updated successfully!")
        return flask.redirect(flask.url_for('index'))


# Delete function
@app.route('/delete/<int:id>/', methods=['GET', 'POST'])
def delete(id):
    session.query(Employee).filter_by(id=id).delete()
    session.commit()
    flask.flash('Employee deleted successfully!')

    return flask.redirect(flask.url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
