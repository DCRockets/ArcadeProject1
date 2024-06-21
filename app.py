from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory data store
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        todos.append({'task': todo, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    todos[todo_id]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todos.pop(todo_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
