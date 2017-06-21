#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def get_tasks():
    print(json.dumps(request.json, indent=4, sort_keys=True))
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)