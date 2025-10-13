from flask import Flask, request, jsonify, abort

app = Flask(__name__)
items = []
current_id = 1

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    global current_id
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Missing 'name' in request data")
    item = {
        'id': current_id,
        'name': data['name']
    }
    items.append(item)
    current_id += 1
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Missing 'name' in request data")
    for item in items:
        if item['id'] == item_id:
            item['name'] = data['name']
            return jsonify(item)
    abort(404, description="Item not found")

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    for item in items:
        if item['id'] == item_id:
            items = [i for i in items if i['id'] != item_id]
            return '', 204
    abort(404, description="Item not found")

app.run()