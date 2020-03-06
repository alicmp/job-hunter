class Ad(db.models):
    __tablename__ = "vow_property_resource"
    TYPES = [("reddit", "craigslist")]

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(URLType, unique=True)
    insert_date = db.Column(db.DateTime, default=datetime.utcnow)
    ad_type = db.Column(ChoiceType(TYPES), default="reddit")
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
