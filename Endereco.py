from flask import Flask, jsonify, request, make_response

from Bd import Enderecos

app = Flask(__name__)

@app.route('/endereco', methods=['GET'])
def obter_endereco():
    return make_response(jsonify('TODOS OS ENDEREÇOS;', Enderecos))

@app.route('/endereco/<int:id>', methods=['GET'])
def obter_endereco_por_id(id):
    for endereco in Enderecos:
        if endereco.get('id') == id:
            return make_response(jsonify('ENDEREÇO SOLICITADO;', endereco) )

@app.route('/endereco/cep/<cep>', methods=['GET'])
def obter_endereco_cep(cep):
    for ceps in Enderecos:
        if ceps ["cep"] == cep:
            return make_response(jsonify('CEP ENCONTRADO !!', ceps))
        
@app.route('/endereco/<int:id>',methods=['PUT'])
def editar_endereco_por_id(id):
    endereco_alterado = request.get_json()
    for indice,endereco in enumerate(Enderecos):
        if endereco.get('id') == id:
            Enderecos[indice].update(endereco_alterado)
            return make_response(jsonify('ENDEREÇO ATUALIZADO',Enderecos [indice]))
        
@app.route('/endereco', methods=['POST'])
def incluir_novo_endereco():
    novo_endereco = request.get_json()
    Enderecos.append(novo_endereco)

    return make_response(jsonify('NOVO ENDEREÇO ADICIONADO !!', Enderecos))

@app.route('/endereco/<int:id>',methods=['DELETE'])
def excluir_endereco(id):
    for indice, endereco in enumerate(Enderecos):
        if endereco.get('id') == id:
            del Enderecos[indice]

    return make_response(jsonify('ENDEREÇO DELETADO COM SUCESSO!!',Enderecos))

app.run()