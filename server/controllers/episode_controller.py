from flask import Blueprint, jsonify
from server.models.episode import Episode
from server.app import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date.isoformat(), 'number': e.number} for e in episodes]) 