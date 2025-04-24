from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

@app.route('/')
def home():
    return render_template('index.html')  # Show the frontend

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if not task:
        return jsonify({'error': 'Task required'}), 400
    new_task = {'id': len(tasks)+1, 'task': task}
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
