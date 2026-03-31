from flask import Flask, request, jsonify
    

app = Flask(__name__)

tareas =[
    { 'id': 1, 'tarea': 'Aprender Flask', 'completada': False },
    { 'id': 2, 'tarea': 'Lavar el coche', 'completada': False }
]

#GET / obtener todas las tareas
@app.route('/api/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(tareas)

#GET / obtener una tarea especifica
def obtener_tarea(tarea_id):
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    if tarea:
        return jsonify(tarea)
    return jsonify({'error': 'Tarea no encontrada'}), 404

#GET / crear una nueva tarea
@app.route('/api/tareas', methods=['POST'])
def crear_tarea():
    nueva_tarea = {
    'id': len(tareas) + 1,
    'tarea': request.json.get('tarea',''),
    'completada': request.json.get('completada', False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

#delete / eliminar una tarea
@app.route('/api/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [t for t in tareas if t['id'] != tarea_id]
    return jsonify({'mensaje': 'Tarea eliminada'}), 200

if __name__ == '__main__':
    app.run(debug=True)