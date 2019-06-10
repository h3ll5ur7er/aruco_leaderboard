# from .database import Database
# from datetime import datetime
from .web_service import run_webserver
def main(host, port):
    # db = Database()
    
    # test_team = db.teams.add(name="test_team")

    # test_driver = db.drivers.add(name="test_driver", team_id=test_team.id)

    # test_car = db.cars.add(name="test_driver", marker=42, driver_id=test_driver.id)

    # test_event = db.events.add(date=datetime.now())

    # test_race = db.races.add(track="test_track", event_id=test_event.id)

    # test_lap = db.laps.add(number=1, race_id=test_race.id)

    # test_result = db.results.add(start=datetime.now(), end=datetime.now(), car_id=test_car.id, lap_id=test_lap.id)

    
    # print(db.results.list_all()[0])
    # print(db.results.list_all()[0].car.driver.team.name)

    run_webserver(host, port)




