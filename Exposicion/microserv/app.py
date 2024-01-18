from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user_routes import user_routes
from user_model import init_db
from flask_cors import CORS

# Crea una instancia de SQLAlchemy sin inicializar la aplicación
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configura la conexión a la base de datos PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5433/expo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa SQLAlchemy con la aplicación
    init_db(app)

    # Registra las rutas del usuario desde user_routes.py
    app.register_blueprint(user_routes)

    CORS(app)

    return app

if __name__ == '__main__':
    app = create_app()
    # Crea las tablas en la base de datos antes de ejecutar la aplicación
    with app.app_context():
        db.create_all()
    app.run(debug=True)
