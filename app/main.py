from flask import Blueprint, request, jsonify
from models import db, Task

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "DevOps Production App is running!"


@main.route("/health")
def health():
    return {"status": "healthy"}


# CREATE TASK
@main.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    task = Task(title=data["title"])

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }), 201


# GET ALL TASKS
@main.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in tasks
    ])


# GET ONE TASK
@main.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    })


# UPDATE TASK
@main.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    if "title" in data:
        task.title = data["title"]

    if "completed" in data:
        task.completed = data["completed"]

    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    })


# DELETE TASK
@main.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"})
