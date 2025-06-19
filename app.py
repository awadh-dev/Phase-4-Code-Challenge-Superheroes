from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///superheroes.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return {'message': 'Superheroes API'}

@app.route('/heroes')
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()]), 200

@app.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict()), 200

@app.route('/powers')
def get_powers():
    return jsonify([power.to_dict() for power in Power.query.all()]), 200

@app.route('/powers/<int:id>')
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    try:
        data = request.get_json()
        if 'description' in data:
            power.description = data['description']
            db.session.commit()
        return jsonify(power.to_dict()), 200
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        new_hp = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(debug=True)
