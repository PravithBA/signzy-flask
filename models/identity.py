from shared.models import db


class IdentityModel(db.Model):
    __tablename__ = "identity_signzy"

    identity_uuid = db.Column(db.BigInt, unique=True, primary_key=True)
    identity_access_token = db.Column(db.String(), unique=True, nullable=False)
    identity_id = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, identity_uuid, identity_access_token, identity_id):
        self.identity_uuid = identity_uuid
        self.identity_access_token = identity_access_token
        self.identity_id = identity_id

    def __repr__(self):
        return f"<Identity {self.identity_id}>"
