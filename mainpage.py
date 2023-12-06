import sqlite3 as sql
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    connection = sql.connect('database.db')
    connection.row_factory = sql.Row
    return connection

def get_project(project_id):
    conn = get_db_connection()
    project = conn.execute('SELECT * FROM projects WHERE id = ?',
                        (project_id,)).fetchone()
    conn.close()
    if project is None:
        abort(404)
    return project

app = Flask(__name__)
app.config['SECRET KEY'] = 'ce917fad9f103bdf3608775e8fb5e89bc75167d829b96988'

users = {'admin': '\xe2\x7fNXv/t\xd6\xec\xec\x01\t\xe3\x1f#\xa3\xc9\xcf\xe5\xae\xd4\xff\xf4m\xbe\xf8\x89\xd3b/h~'}

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/list')
def project_list():
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    return render_template('project_list.html', projects=projects)

@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

@app.route('/<int:project_id>/edit/', methods = ('GET', 'POST'))
def edit(project_id):
    project = get_project(project_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date_created = request.form['date_created']
        github_link = request.form['github_link']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        elif not date_created:
            flash('Date is required!')
        else:
            conn = get_db_connection
            conn.execute('UPDATE projects set title = ?, content = ?, date_created = ?, github_link = ?'
                         ' WHERE id = ?',
                         (title, content, date_created, github_link, project_id))
            conn.commit()
            conn.close()
            return redirect(url_for('project_list'))
    return render_template('edit.html', project = project)

@app.route("/create/", methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date_created = request.form['date_created']
        github_link = request.form['github_link']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        elif not date_created:
            flash('Date is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)',
                         (title, content, date_created, github_link))
            conn.commit()
            conn.close()
            return redirect(url_for('project_list'))
    return render_template('creator_page.html')

@app.route("/<int:id>/delete/", methods=("POST",))
def delete(id):
    project = get_project(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM projects WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(project['title']))
    return render_template('project_list.html')

