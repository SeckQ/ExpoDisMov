from flask import Blueprint, request, jsonify
from user_model import db, User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birthdate': str(user.birthdate),
            'nickname': user.nickname,
            'occupation': user.occupation,
            'photo': user.photo
        })
    return jsonify({'users': user_list})


@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json

    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        birthdate=data['birthdate'],
        nickname=data['nickname'],
        occupation=data['occupation'],
        photo=data['photo']
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Usuario creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()


@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birthdate': str(user.birthdate),
            'nickname': user.nickname,
            'occupation': user.occupation,
            'photo': user.photo
        })
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404


@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.json

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.birthdate = data.get('birthdate', user.birthdate)
        user.nickname = data.get('nickname', user.nickname)
        user.occupation = data.get('occupation', user.occupation)
        user.photo = data.get('photo', user.photo)

        try:
            db.session.commit()
            return jsonify({'message': 'Usuario actualizado correctamente'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        finally:
            db.session.close()
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404


@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'Usuario eliminado correctamente'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        finally:
            db.session.close()
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404


