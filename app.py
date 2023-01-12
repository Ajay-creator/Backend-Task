from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
# Change the URI with the actual URI of a DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://username:password@host:port/dbname'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    num_likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    likes = db.relationship('Like', backref='message', lazy=True)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.route('/messages', methods=['POST'])
def create_message():
    message = request.json['message']
    new_message = Message(message=message)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Successfully created message.'}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return jsonify([{'id': message.id, 'message': message.message, 'num_likes': message.num_likes, 'created_at': message.created_at.isoformat()} for message in messages]), 200

@app.route('/messages/<int:message_id>/like', methods=['POST'])
def like_message(message_id):
    new_like = Like(message_id=message_id)
    db.session.add(new_like)
    db.session.commit()
    return jsonify({'message': 'Successfully liked message.'}), 201

@app.route('/messages/<int:message_id>/like', methods=['DELETE'])
def unlike_message(message_id):
    like = Like.query.filter_by(message_id=message_id).first()
    db.session.delete(like)
    db.session.commit()
    return jsonify({'message': 'Successfully unliked message.'}), 200
