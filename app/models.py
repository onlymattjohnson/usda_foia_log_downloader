from app import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_no = db.Column(db.String(32), index=True, unique=True)
    date_received = db.Column(db.DateTime)
    date_due = db.Column(db.DateTime, index=True)
    date_closed = db.Column(db.DateTime, index=True)
    track = db.Column(db.String(32))
    subject = db.Column(db.String(500))

    def __repr__(self):
        return '<Case %r> %r' % (self.case_no, self.subject)    