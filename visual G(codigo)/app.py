from flask import Flask, request, jsonify
from flask_cors import CORS
from conexao import conectar

app = Flask(__name__)
CORS(app)  # permite o HTML chamar o servidor

# ──────────────────────────────
# GET - Exibir planos no site
# ──────────────────────────────
@app.route("/planos", methods=["GET"])
def get_planos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)  # retorna como dicionário
    cursor.execute("SELECT * FROM planos")
    planos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(planos)

# ──────────────────────────────
# GET - Exibir unidades no site
# ──────────────────────────────
@app.route("/unidades", methods=["GET"])
def get_unidades():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM unidades")
    unidades = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(unidades)

# ──────────────────────────────
# GET - Exibir clientes cadastrados
# ──────────────────────────────
@app.route("/clientes", methods=["GET"])
def get_clientes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT c.id_cliente, c.nome, c.telefone, c.plano_id, p.nome AS plano_nome "
        "FROM clientes c LEFT JOIN planos p ON c.plano_id = p.id_plano"
    )
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(clientes)

# ──────────────────────────────
# PUT - Atualizar matrícula
# ──────────────────────────────
@app.route("/matricula/<int:id_cliente>", methods=["PUT"])
def put_matricula(id_cliente):
    dados = request.json
    nome     = dados.get("nome")
    telefone = dados.get("telefone")
    plano_id = dados.get("plano_id")

    if not nome or not telefone or not plano_id:
        return jsonify({"erro": "Preencha todos os campos"}), 400

    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "UPDATE clientes SET nome = %s, telefone = %s, plano_id = %s WHERE id_cliente = %s"
        cursor.execute(sql, (nome, telefone, plano_id, id_cliente))
        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return jsonify({"erro": "Cliente não encontrado"}), 404
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensagem": f"Cliente {nome} atualizado com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ──────────────────────────────
# DELETE - Excluir matrícula
# ──────────────────────────────
@app.route("/matricula/<int:id_cliente>", methods=["DELETE"])
def delete_matricula(id_cliente):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(sql, (id_cliente,))
        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return jsonify({"erro": "Cliente não encontrado"}), 404
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensagem": "Cliente excluído com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ──────────────────────────────
# POST - Salvar matrícula (cliente)
# ──────────────────────────────
@app.route("/matricula", methods=["POST"])
def post_matricula():
    dados = request.json
    nome     = dados.get("nome")
    telefone = dados.get("telefone")
    plano_id = dados.get("plano_id")

    if not nome or not telefone or not plano_id:
        return jsonify({"erro": "Preencha todos os campos"}), 400

    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nome, telefone, plano_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, telefone, plano_id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensagem": f"Cliente {nome} cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ──────────────────────────────
# POST - Salvar interesse em franquia
# ──────────────────────────────
@app.route("/franquia", methods=["POST"])
def post_franquia():
    dados = request.json
    nome             = dados.get("nome")
    telefone         = dados.get("telefone")
    cidade_interesse = dados.get("cidade_interesse")

    if not nome or not telefone or not cidade_interesse:
        return jsonify({"erro": "Preencha todos os campos"}), 400

    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO franquias (nome, telefone, cidade_interesse) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, telefone, cidade_interesse))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensagem": f"Interesse de {nome} registrado!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ──────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)  # roda em http://localhost:5000