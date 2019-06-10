
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import relationship, deferred
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, select, func

Model = declarative_base()




class Team(Model):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    members = relationship("Driver", back_populates="team")
    def __str__(self):
        return f"Team(id={self.id}, name={self.name})"


class Driver(Model):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship("Team", back_populates="members")
    cars = relationship("Car", back_populates="driver")
    def __str__(self):
        return f"Driver(id={self.id}, team={self.name})"


class Car(Model):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    marker = Column(Integer, nullable=True)
    driver_id = Column(Integer, ForeignKey('driver.id'))
    driver = relationship("Driver", back_populates="cars")
    results = relationship("Result", back_populates="car")
    def __str__(self):
        return f"Car(id={self.id}, marker={self.marker}, driver={self.driver})"


class Event(Model):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    races = relationship("Race", back_populates="event")
    def __str__(self):
        return f"Event(id={self.id}, date={self.date})"


class Race(Model):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    track = Column(String(150), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'))
    event = relationship("Event", back_populates="races")
    laps = relationship("Lap", uselist=True, back_populates="race")
    def __str__(self):
        return f"Race(id={self.id}, name={self.name})"

class Lap(Model):
    __tablename__ = 'lap'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    race_id = Column(Integer, ForeignKey('race.id'))
    race = relationship("Race", back_populates="laps")
    results = relationship("Result", back_populates="lap")
    def __str__(self):
        return f"Lap(id={self.id}, name={self.name})"


class Result(Model):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    car_id = Column(Integer, ForeignKey('car.id'))
    car = relationship("Car", back_populates="results")
    lap_id = Column(Integer, ForeignKey('lap.id'))
    lap = relationship("Lap", back_populates="results")


