from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista inicial de tareas
todo_list = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    },
    {
        "done": False,
        "label": "Sample Todo 3"
    },
    {
        "done": True,
        "label": "Sample Todo 4"
    }
]

# Endpoint para obtener todas las tareas
@app.route("/todos", methods=['GET'])
def get_todos():
    return jsonify(todo_list), 200

# Endpoint para agregar una nueva tarea
@app.route("/todos", methods=['POST'])
def add_todo():
    body = request.get_json()
    if body is None:
        return "El cuerpo de la solicitud es null", 400
    if 'done' not in body or 'label' not in body:
        return 'Debes especificar "done" y "label"', 400
    
    todo_list.append(body)  # Agrega la nueva tarea a la lista
    return jsonify(todo_list), 201

# Endpoint para eliminar una tarea por posición
@app.route("/todos/<int:position>", methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todo_list):
        return "Índice fuera de rango", 404
    
    removed_todo = todo_list.pop(position)  # Elimina la tarea de la lista
    return jsonify(removed_todo), 200

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(host='0.0.0.0')