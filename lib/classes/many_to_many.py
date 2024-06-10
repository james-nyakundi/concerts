import os
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
sys.path.append(os.getcwd)


engine = create_engine('sqlite:///lib/db/concerts.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    concerts = relationship('Concert', back_populates='band')

    def concerts(self):
         return self.concerts
        

    def venues(self):
         return [concert.venue for concert in self.concerts]
        

    def play_in_venue(self, venue, date):
         concert = Concert(date=date, band=self, venue=venue)
        

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]
        


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    concerts = relationship('Concert')

    def hometown_show(self):
         return self.band.hometown == self.venue.city

    def introduction(self):
         return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def concerts(self):
         return self.concerts

    def bands(self):
         return [concert.band for concert in self.concerts]