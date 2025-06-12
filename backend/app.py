from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "description": self.description
        }

@app.route('/')
def home():
    return {"message": "E-commerce chatbot backend is running!"}

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    results = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    return jsonify([p.to_dict() for p in results])

if __name__ == '__main__':
    app.run(debug=True)
