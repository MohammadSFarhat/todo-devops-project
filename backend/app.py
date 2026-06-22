from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "running",
        "service": "todo-backend"
    }), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400

    task = {
        "id": len(tasks),
        "task": data["task"],
        "done": False
    }

    tasks.append(task)

    return jsonify({
        "message": "Task added",
        "task": task
    }), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    task_to_delete = next((task for task in tasks if task["id"] == task_id), None)

    if task_to_delete is None:
        return jsonify({"error": "Task not found"}), 404

    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({"message": "Task deleted"}), 200

@app.route("/tasks/<int:task_id>/done", methods=["PUT"])
def mark_task_done(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    task["done"] = True

    return jsonify({
        "message": "Task marked as done",
        "task": task
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)