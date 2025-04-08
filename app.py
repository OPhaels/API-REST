from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados simulada
users = {
    1: {"name": "Laysa", "email": "laysa@test.com"},
    2: {"name": "Raphael", "email": "joao@test.com"}
}

# Rota principal
@app.route('/')
def home():
    return jsonify({"message": "API REST Simples com Flask"})

# Obter todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Obter um usuário por ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "Usuário não encontrado"}), 404

# Criar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

# Atualizar um usuário existente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify(users[user_id])
    return jsonify({"error": "Usuário não encontrado"}), 404

# Deletar um usuário
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "Usuário deletado com sucesso"})
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
