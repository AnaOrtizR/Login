from flask import Blueprint, request, jsonify
from app.models import db, Users
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    try:
        list_users  = Users.query.all()
        return jsonify([{'id': users.id,
                         'fullName':users.fullName,
                         'username': users.username,
                         'email': users.email,
                         'passwd': users.passwd,
                         'dateCreated':users.dateCreated,
                         'dateUpdated':users.dateUpdated
                         }
                         for users in list_users ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route('/newUser', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    try:
        user = Users.query.filter_by(username=username).first()
        if user:
            return jsonify({"message": "El username ya está registrado."}), 401
        else:
            new_user = Users(fullName=data['fullName'],
                            username=data['username'],
                            email=data['email'],
                            passwd=data['passwd'])
            db.session.add(new_user)
            db.session.commit()
            return jsonify ({'id': new_user.id,
                         'fullName':new_user.fullName,
                         'username': new_user.username,
                         'email': new_user.email,
                         'passwd': new_user.passwd,
                         'dateCreated':new_user.dateCreated,
                         'dateUpdated':new_user.dateUpdated
                         }), 201
    except:
        return jsonify({"message": "Hubo un problema al registrar"}), 401
    
@users_bp.route('/LoginUser', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('passwd')
    print(username, " ",password)
    try:
        user = Users.query.filter_by(username=username).first()

        if user and user.check_password(password):
            token = create_access_token(identity=username)
            return jsonify({"message": "Login successful", "token": token}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    except:
        return jsonify({"message": "Hubo un problema al buscar al validar"}), 401
    
@users_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    current_user = get_jwt_identity()
    usuario = Users.query.filter_by(username=current_user).first()
    if usuario:
        info = usuario.personal_info()
        return jsonify(logged_in_as=current_user, data=info), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404