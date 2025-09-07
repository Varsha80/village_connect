from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///village.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        user_id = request.form['user_id']
        new_service = Service(
            title=title,
            description=description,
            location=location,
            user_id=int(user_id)
        )
        db.session.add(new_service)
        db.session.commit()
        return redirect('/services')

    search = request.args.get('search')
    if search:
        services = Service.query.filter(
            Service.title.contains(search) | 
            Service.description.contains(search)
        ).all()
    else:
        services = Service.query.all()
    return render_template('services.html', services=services)


@app.route('/delete_service/<int:service_id>', methods=['POST'])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect('/services')


@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        content = request.form['content']
        user_id = request.form['user_id']
        new_post = Post(content=content, user_id=int(user_id))
        db.session.add(new_post)
        db.session.commit()
        return redirect('/forum')

    posts = Post.query.all()
    return render_template('forum.html', posts=posts)


@app.route('/api/services', methods=['GET'])
def api_get_services():
    search = request.args.get('search')
    if search:
        services = Service.query.filter(
            Service.title.contains(search) |
            Service.description.contains(search)
        ).all()
    else:
        services = Service.query.all()

    result = [{
        "id": s.id,
        "title": s.title,
        "description": s.description,
        "location": s.location,
        "user_id": s.user_id
    } for s in services]

    return jsonify(result), 200


@app.route('/api/services', methods=['POST'])
def api_create_service():
    data = request.get_json()
    required = ['title', 'description', 'location', 'user_id']

    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    new_service = Service(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        user_id=int(data['user_id'])
    )

    db.session.add(new_service)
    db.session.commit()

    return jsonify({
        "message": "Service created successfully",
        "id": new_service.id
    }), 201
    

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

