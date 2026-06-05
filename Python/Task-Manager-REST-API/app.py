from flask import Flask, jsonify, request
import json

app = Flask(__name__)

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1

@app.route("/")
def home():
    return "Welcome to the Task Manager API!"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = load_tasks()

    data = request.get_json()

    task = {
        "id": generate_id(tasks),
        "title": data["title"],
        "priority": data["priority"],
        "status": "Pending",
        "due_date": data["due_date"]
    }

    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    tasks = load_tasks()

    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = data.get("title", task["title"])
            task["priority"] = data.get("priority", task["priority"])
            task["status"] = data.get("status", task["status"])
            task["due_date"] = data.get("due_date", task["due_date"])

            save_tasks(tasks)

            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            return jsonify({
                "message": "Task deleted successfully"
            })

    return jsonify({
        "error": "Task not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)

