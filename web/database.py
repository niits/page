from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict


migrate = Migrate()
db = SQLAlchemy()


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    hash_id=db.Column(db.String(256), nullable=False)
    ip_address = db.Column(db.String(256), nullable=False)
    path = db.Column(db.String(256), nullable=False)
    time = db.Column(db.DateTime)
    user_agent = db.Column(db.String(256))
    status = db.Column(db.Integer)
    method = db.Column(db.String(4))
    size = db.Column(db.Integer)
    referrer = db.Column(db.String(256))
    fingerprint = db.Column(db.String(2560))

    def __repr__(self):
        return u'<Request %s>'.format(self.id)


class DetectionTime(db.Model):
    __tablename__ = 'detection_times'

    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(256), nullable=False)
    date = db.Column(db.Time)
    hour = db.Column(db.Integer)
    reason = db.Column(db.String(256))
    ban_expired_at = db.Column(db.DateTime)

    def __repr__(self):
        return u'<DetectionTimes %s>'.format(self.id)