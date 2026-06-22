from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    if id < len(tasks):
        tasks.pop(id)
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)