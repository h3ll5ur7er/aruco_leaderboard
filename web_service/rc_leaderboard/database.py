
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, joinedload
from .framework import Singleton, Repository
from .data_model import Model, Car, Driver, Team, Event, Race, Lap, Category, Result

class Db(metaclass=Singleton):
    def __init__(self):
        self._db_name = "leaderboard.db"
        self.engine   = create_engine("sqlite:///{}".format(self._db_name))
        self.session  = create_session(self.engine)
        from os.path import exists
        if not exists(self._db_name):
            Model.metadata.create_all(self.engine)
    def query(self, *a, **kw):
        return self.session.query(*a, **kw)
    def add(self, entity):
        self.session.add(entity)
        self.session.flush()
        return entity
    def remove(self, entity):
        self.session.delete(entity)
        self.session.flush()


class GenericRepository(Repository):
    def __init__(self, datatype):
        self._datatype = datatype
    def add(self, *a, **kw):
        return Db().add(self._datatype(*a, **kw))
    def remove(self, entity):
        Db().remove(entity)
    def commit(self):
        Db().session.flush()
    def update(self, entity):
        Db().session.flush()
    def get_by_id(self, id):
        return Db().query(self._datatype).options(joinedload("*")).get(id)
    def list_all(self):
        return Db().query(self._datatype).options(joinedload("*")).all()
    

class CarRepository(GenericRepository):
    def __init__(self):
        super().__init__(Car)


class DriverRepository(GenericRepository):
    def __init__(self):
        super().__init__(Driver)


class TeamRepository(GenericRepository):
    def __init__(self):
        super().__init__(Team)


class EventRepository(GenericRepository):
    def __init__(self):
        super().__init__(Event)


class RaceRepository(GenericRepository):
    def __init__(self):
        super().__init__(Race)


class LapRepository(GenericRepository):
    def __init__(self):
        super().__init__(Lap)

class CategoryRepository(GenericRepository):
    def __init__(self):
        super().__init__(Category)

class ResultRepository(GenericRepository):
    def __init__(self):
        super().__init__(Result)



class Database(metaclass=Singleton):
    def __init__(self):
        self.categories = CategoryRepository()
        self.cars = CarRepository()
        self.drivers = DriverRepository()
        self.teams = TeamRepository()
        self.events = EventRepository()
        self.races = RaceRepository()
        self.laps = LapRepository()
        self.results = ResultRepository()

