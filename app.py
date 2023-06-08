import sqlite3
from flask import Flask, render_template, request
from dbconnection import createconnection

app = Flask(__name__)
string = '''
<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>
'''
string2 = '<ul><li>' + '150' + '</li><li>' + \
    'blue' + '</li><li>' + 'jeep'+'</li></ul>'


@app.route("/test2")
def test2():
    name = 'Tay'
    message1 = 'welcome'
    message2 = 'hello'
    return render_template('test2.html', name=name, message1=message1, message2=message2)


@app.route("/test3")
def test3():

    foods = [{'name': 'pizza'}, {'name': 'sushi'},
             {'name': 'burger'}, {'name': 'pasta'}]
    return render_template('test3.html', foods=foods)
    # greeting = 'greetings'
    # users = [{'name': 'Tay'},{'name': 'Ray'},{'name': 'tommy'}]
    # return render_template('test3.html', greeting=greeting, users=users)
    # return render_template('test3.html', greetinghtml=greeting, userhtml=user['name'])


@app.route("/testb")
def testb():
    return render_template('testb.html')


@app.route("/")
def hello():
    return string


@app.route("/test4")
def test4():
    return render_template('test4.html')


@app.route("/test")
def test():
    return render_template('test.html')
# greeting = 'hello'
# user = {'name': 'Tay'}
# return '<h1>' + greeting + ' ' + user['name'] + ' </h1>'


@app.route("/cars")
def car():
    car = {'speed': '150', 'color': 'blue', 'brand': 'jeep'}
    return '<ul><li>' + car['speed'] + '</li><li>' + car['color'] + ' </li><li>' + car['brand']+'</li></ul>'

    # return '<h1> This ' + car['color'] + ' ' + car['brand'] + ' ' + 'can drive up to' + ' ' + car['speed'] + ' ' + 'Miles per hour!!!' + '</h1>'


@app.route("/handlemessage", methods=["post"])
def handlemessage():
    msg = request.form["message"]
    msg1 = request.form["age"]
    print(msg)
    print(msg1)
    return render_template('result.html', msg=msg, msg1=msg1)


@app.route("/base")
def base():
    return render_template('base.html')


@app.route("/form")
def form():
    return render_template('form.html')


def retrieve_books():
    connection = createconnection()
    cur = connection.cursor()
    cur.execute("select * from books")
    rows = cur.fetchall()
    print(rows)
    for row in rows:
        print(row)


@app.route("/viewauthors")
def retrieveauthors():
    connection = createconnection()
    cur = connection.cursor()
    cur.execute("select * from author")
    rows = cur.fetchall()
    print(rows)
    # for row in rows:
    # print(row)
    return render_template("viewauthors.html", authors=rows)


if __name__ == "__main__":
    retrieveauthors()


@app.route("/viewbooks")
def retrievebooks():
    connection = createconnection()
    cur = connection.cursor()
    cur.execute(
        "select b.id, b.title, b.main_character, a.name from books b inner join author a on b.author_id=a.id")
    rows = cur.fetchall()
    print(rows)
    # for row in rows:
    # print(row)
    return render_template("viewbooks.html", books=rows)

    # createconnection()
