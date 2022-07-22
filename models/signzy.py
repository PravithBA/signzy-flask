from shared.models import db
from sqlalchemy.dialects.postgresql import ARRAY


class IdentityModel(db.Model):
    __tablename__ = "identity_signzy"

    identity_access_token = db.Column(db.String(), unique=True, nullable=False)
    identity_id = db.Column(db.String(), unique=True, nullable=False, primary_key=True)

    def __init__(self, identity_access_token, identity_id):
        self.identity_access_token = identity_access_token
        self.identity_id = identity_id

    def __repr__(self):
        return f"<Identity {self.identity_id}>"


class AadharModel(db.Model):
    __tablename__ = "aadhar_signzy"

    aadhar_number = db.Column(db.BigInteger(), unique=True, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    dob = db.Column(db.String(), unique=True, nullable=False)
    address_str = db.Column(db.String(), unique=True, nullable=False)
    state = db.Column(ARRAY(db.String()), unique=True, nullable=False)
    city = db.Column(ARRAY(db.String()), unique=True, nullable=False)
    district = db.Column(ARRAY(db.String()), unique=True, nullable=False)
    pincode = db.Column(db.BigInteger(), unique=True, nullable=False)
    address_line = db.Column(db.String(), unique=True, nullable=False)
    gender = db.Column(db.String(), unique=True, nullable=False)
    guardian = db.Column(db.String(), unique=True, nullable=False)
    expiry_date = db.Column(db.String(), unique=True, nullable=False)
    issue_date = db.Column(db.String(), unique=True, nullable=False)

    def __init__(
        self,
        aadhar_number,
        name,
        dob,
        address_str,
        state,
        city,
        district,
        pincode,
        address_line,
        gender,
        guardian,
        expiry_date,
        issue_date,
    ):
        self.aadhar_number = aadhar_number
        self.name = name
        self.dob = dob
        self.address_str = address_str
        self.state = state
        self.city = city
        self.district = district
        self.pincode = pincode
        self.address_line = address_line
        self.gender = gender
        self.guardian = guardian
        self.expiry_date = expiry_date
        self.issue_date = issue_date

    def __repr__(self):
        return f"<Identity {self.aadhar_number}>"
