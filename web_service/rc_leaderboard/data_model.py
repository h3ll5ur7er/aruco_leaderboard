
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import relationship, deferred
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, select, func

Model = declarative_base()




class Team(Model):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cars = relationship("Car", back_populates="team")
    def __str__(self):
        return "Team(id={}, name={})".format(self.id, self.name)


class Driver(Model):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cars = relationship("Car", back_populates="driver")
    def __str__(self):
        return "Driver(id={}, name={}, team={})".format(self.id, self.name, self.team)

class Category(Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cars = relationship("Car", back_populates="category")
    def __str__(self):
        return "Category(id={}, name={})".format(self.id, self.name)


class Car(Model):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    marker1 = Column(Integer, nullable=True)
    marker2 = Column(Integer, nullable=True)
    marker3 = Column(Integer, nullable=True)
    marker4 = Column(Integer, nullable=True)
    driver_id = Column(Integer, ForeignKey('driver.id'))
    driver = relationship("Driver", back_populates="cars")
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="cars")
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship("Team", back_populates="cars")
    results = relationship("Result", back_populates="car")
    def __str__(self):
        return "Car(id={}, markers=({}, {}, {}, {}), driver={})".format(self.id, self.marker1, self.marker2, self.marker3, self.marker4, self.driver)


class Event(Model):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    races = relationship("Race", back_populates="event")
    def __str__(self):
        return "Event(id={}, date={})".format(self.id, self.date)


class Race(Model):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    track = Column(String(150), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'))
    event = relationship("Event", back_populates="races")
    laps = relationship("Lap", uselist=True, back_populates="race")
    def __str__(self):
        return "Race(id={}, name={})".format(self.id, self.name)

class Lap(Model):
    __tablename__ = 'lap'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    race_id = Column(Integer, ForeignKey('race.id'))
    race = relationship("Race", back_populates="laps")
    results = relationship("Result", back_populates="lap")
    def __str__(self):
        return "Lap(id={}, name={})".format(self.id, self.name)


class Result(Model):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    car_id = Column(Integer, ForeignKey('car.id'))
    car = relationship("Car", back_populates="results")
    lap_id = Column(Integer, ForeignKey('lap.id'))
    lap = relationship("Lap", back_populates="results")
    def __str__(self):
        return "Result(id={}, car={}, lap={})".format(self.id, self.name)


