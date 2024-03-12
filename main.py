from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/RickAndMorty'
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS (app)

# Classe para representar a tabela 'characters'
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(20))
    species = db.Column(db.String(50))
    type = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    origin_name = db.Column(db.String(50))
    location_name = db.Column(db.String(50))
    image = db.Column(db.String(100))

class CharacterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status', 'species', 'type', 'gender', 'origin_name', 'location_name', 'image')

character_schema = CharacterSchema(many=True)

# Rota para retornar todos os dados agrupados em grupos de 20 itens
@app.route('/search', methods=['GET'])
def get_characters():
    name = request.args.get('name')
    page = int(request.args.get('page', default=1))
    print (page, name)
    per_page = int(request.args.get('per_page', default=20))
    characters = Character.query.filter(Character.name.ilike(f"%{name}%")).order_by(Character.id.asc()).paginate(page=page, per_page=per_page)

    # data = [{'id': character.id, 'name': character.name, 'status': character.status, 'species': character.species,
    #          'type': character.type, 'gender': character.gender, 'origin_name': character.origin_name,
    #          'location_name': character.location_name, 'image': character.image} for character in characters]
    return jsonify({
        'page': characters.page,
        'total_page': characters.pages,
        'items': character_schema.dump(characters.items)
    })

# Rota para retornar um único item pelo id
@app.route('/search/<int:id>', methods=['GET'])
def get_by_id(id):
    character = Character.query.get(id)
    if character:
        data = {'id': character.id, 'name': character.name, 'status': character.status, 'species': character.species,
                'type': character.type, 'gender': character.gender, 'origin_name': character.origin_name,
                'location_name': character.location_name, 'image': character.image}
        return jsonify(data)
    else:
        return jsonify({'message': 'Character not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
