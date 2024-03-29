from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(5000))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(500))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
        scheme = {"id": self.id,
                  "name": self.name,
                  "genres": self.genres,
                  "address": self.address,
                  "city": self.city,
                  "state": self.state,
                  "phone": self.phone,
                  "website": self.website,
                  "facebook_link": self.facebook_link,
                  "seeking_talent": self.seeking_talent,
                  "seeking_description": self.seeking_description,
                  "image_link": self.image_link,
                  "past_shows": [],
                  "upcoming_shows": [],
                  "past_shows_count": 0,
                  "upcoming_shows_count": 0,
                  }

        return f'{scheme}'


# TODO: implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(5000))
    website_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        scheme = {"id": self.id,
                  "name": self.name,
                  "genres": self.genres,
                  "address": self.address,
                  "city": self.city,
                  "state": self.state,
                  "phone": self.phone,
                  "facebook_link": self.facebook_link,
                  "website_link": self.website_link,
                  "seeking_venue": self.seeking_talent,
                  "seeking_description": self.seeking_description,
                  "image_link": self.image_link,
                  "past_shows": [],
                  "upcoming_shows": [],
                  "past_shows_count": 0,
                  "upcoming_shows_count": 0
                  }

        return f'{scheme}'


class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime(), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.