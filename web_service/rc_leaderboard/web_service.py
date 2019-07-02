from flask import Flask, request, send_file
from flask_restplus import Api, Resource
from flask_restplus.fields import String, Integer, DateTime, List, Nested
from werkzeug.datastructures import FileStorage
from io import BytesIO
from .marker_detection import MarkerDetector
from .marker import MarkerRegistry
from .database import Database


def setup_api():
    app = Flask("Leaderboard")
    api = Api(app)

    ### MODELS ###
    image_upload_parser = api.parser()
    image_upload_parser.add_argument('file', location='files', type=FileStorage, required=True)
    marker_model = api.model("Marker", {
        "id": Integer
    })
    markers_model = api.model("Markers", {"ids":List(String)})
    team_model = api.model("Team", {
        "id": Integer,
        "name": String
    })
    teams_model = api.model("Teams", {"teams":List(Nested(team_model))})
    driver_model = api.model("Driver", {
        "id": Integer,
        "name": String
    })
    drivers_model = api.model("Drivers", {"drivers":List(Nested(driver_model))})
    category_model = api.model("Category", {
        "id": Integer,
        "name": String
    })
    categories_model = api.model("Categories", {"categories":List(Nested(category_model))})
    car_model = api.model("Car", {
        "id": Integer,
        "marker1": Integer,
        "marker2": Integer,
        "marker3": Integer,
        "marker4": Integer,
        "driver_id": Integer,
        "team_id": Integer,
        "category_id": Integer
    })
    cars_model = api.model("Cars", {"cars":List(Nested(car_model))})
    event_model = api.model("Event", {
        "id": Integer,
        "date": DateTime
    })
    events_model = api.model("Events", {"events":List(Nested(event_model))})
    race_model = api.model("Race", {
        "id": Integer,
        "track": String,
        "event_id": Integer
    })
    races_model = api.model("Races", {"races":List(Nested(race_model))})
    lap_model = api.model("Lap", {
        "id": Integer,
        "number": Integer,
        "race_id": Integer
    })
    laps_model = api.model("Laps", {"laps":List(Nested(lap_model))})
    result_model = api.model("Result", {
        "id": Integer,
        "start": DateTime,
        "end": DateTime,
        "car_id": Integer,
        "lap_id": Integer
    })
    results_model = api.model("Results", {"results":List(Nested(result_model))})
    

    ### TEAM ###
    @api.route("/team")
    class AllTeamsEndpoint(Resource):
        @api.marshal_with(teams_model)
        def get(self):
            return {"teams":Database().teams.list_all()}
        @api.expect(team_model, validate=True)
        @api.marshal_with(team_model)
        def post(self):
            params = request.json
            print("adding team with params: ", params)
            return Database().teams.add(**params), 200
    
    @api.route("/team/<int:id>")
    class OneTeamsEndpoint(Resource):
        @api.marshal_with(team_model)
        def get(self, id):
            return Database().teams.get_by_id(id)
            
        @api.expect(team_model, validate=True)
        @api.marshal_with(team_model)
        def post(self, id):
            params = request.json
            current = Database().teams.get_by_id(id)
            current.name = params["name"]
            Database().teams.commit()
            return current


    ### DRIVER ###
    @api.route("/driver")
    class AllDriversEndpoint(Resource):
        @api.marshal_with(drivers_model)
        def get(self):
            return {"drivers":Database().drivers.list_all()}
        @api.expect(driver_model, validate=True)
        @api.marshal_with(driver_model)
        def post(self):
            params = request.json
            return Database().drivers.add(**params), 200
    
    @api.route("/driver/<int:id>")
    class OneDriverEndpoint(Resource):
        @api.marshal_with(driver_model)
        def get(self, id):
            return Database().drivers.get_by_id(id)
            
        @api.expect(driver_model, validate=True)
        @api.marshal_with(driver_model)
        def post(self, id):
            params = request.json
            current = Database().drivers.get_by_id(id)
            current.name = params["name"]
            Database().drivers.commit()
            return current


    ### CATEGORY ###
    @api.route("/category")
    class AllCategoriesEndpoint(Resource):
        @api.marshal_with(categories_model)
        def get(self):
            return {"drivers":Database().categories.list_all()}
        @api.expect(category_model, validate=True)
        @api.marshal_with(category_model)
        def post(self):
            params = request.json
            return Database().categories.add(**params), 200
    
    @api.route("/category/<int:id>")
    class OneCategoryEndpoint(Resource):
        @api.marshal_with(category_model)
        def get(self, id):
            return Database().category.get_by_id(id)
            
        @api.expect(category_model, validate=True)
        @api.marshal_with(category_model)
        def post(self, id):
            params = request.json
            current = Database().categories.get_by_id(id)
            current.name = params["name"]
            Database().categories.commit()
            return current


    ### CAR ###
    @api.route("/car")
    class AllCarsEndpoint(Resource):
        @api.marshal_with(cars_model)
        def get(self):
            return {"cars":Database().cars.list_all()}
        @api.expect(car_model, validate=True)
        @api.marshal_with(car_model)
        def post(self):
            params = request.json
            return Database().cars.add(**params), 200
    
    @api.route("/car/<int:id>")
    class OneCarEndpoint(Resource):
        @api.marshal_with(car_model)
        def get(self, id):
            return Database().cars.get_by_id(id)
            
        @api.expect(car_model, validate=True)
        @api.marshal_with(car_model)
        def post(self, id):
            params = request.json
            current = Database().cars.get_by_id(id)
            current.marker = params["marker"]
            current.driver_id = params["driver_id"]
            Database().cars.commit()
            return current


    ### EVENT ###
    @api.route("/event")
    class AllEventsEndpoint(Resource):
        @api.marshal_with(events_model)
        def get(self):
            return {"events":Database().events.list_all()}
        @api.expect(event_model, validate=True)
        @api.marshal_with(event_model)
        def post(self):
            params = request.json
            return Database().events.add(**params), 200
    
    @api.route("/event/<int:id>")
    class OneEventEndpoint(Resource):
        @api.marshal_with(event_model)
        def get(self, id):
            return Database().events.get_by_id(id)
            
        @api.expect(event_model, validate=True)
        @api.marshal_with(event_model)
        def post(self, id):
            params = request.json
            current = Database().events.get_by_id(id)
            current.date = params["date"]
            Database().events.commit()
            return current


    ### RACE ###
    @api.route("/race")
    class AllRacesEndpoint(Resource):
        @api.marshal_with(races_model)
        def get(self):
            return {"races":Database().races.list_all()}
        @api.expect(race_model, validate=True)
        @api.marshal_with(race_model)
        def post(self):
            params = request.json
            return Database().races.add(**params), 200
    
    @api.route("/race/<int:id>")
    class OneRaceEndpoint(Resource):
        @api.marshal_with(race_model)
        def get(self, id):
            return Database().races.get_by_id(id)
            
        @api.expect(race_model, validate=True)
        @api.marshal_with(race_model)
        def post(self, id):
            params = request.json
            current = Database().races.get_by_id(id)
            current.track = params["track"]
            current.event_id = params["event_id"]
            Database().races.commit()
            return current


    ### LAP ###
    @api.route("/lap")
    class AllLapEndpoint(Resource):
        @api.marshal_with(laps_model)
        def get(self):
            return {"laps":Database().laps.list_all()}
        @api.expect(lap_model, validate=True)
        @api.marshal_with(lap_model)
        def post(self):
            params = request.json
            return Database().laps.add(**params), 200
    
    @api.route("/lap/<int:id>")
    class OneLapEndpoint(Resource):
        @api.marshal_with(lap_model)
        def get(self, id):
            return Database().laps.get_by_id(id)
            
        @api.expect(lap_model, validate=True)
        @api.marshal_with(lap_model)
        def post(self, id):
            params = request.json
            current = Database().lap.get_by_id(id)
            current.track = params["number"]
            current.race_id = params["race_id"]
            Database().laps.commit()
            return current


    ### RESULT ###
    @api.route("/result")
    class AllResultsEndpoint(Resource):
        @api.marshal_with(results_model)
        def get(self):
            return {"results":Database().results.list_all()}
        @api.expect(result_model, validate=True)
        @api.marshal_with(result_model)
        def post(self):
            params = request.json
            return Database().results.add(**params), 200
    
    @api.route("/result/<int:id>")
    class OneResultEndpoint(Resource):
        @api.marshal_with(result_model)
        def get(self, id):
            return Database().results.get_by_id(id)
            
        @api.expect(result_model, validate=True)
        @api.marshal_with(result_model)
        def post(self, id):
            params = request.json
            current = Database().results.get_by_id(id)
            current.start = params["start"]
            current.end = params["end"]
            current.lap_id = params["lap_id"]
            Database().results.commit()
            return current


    # Infrastructure
    @api.route("/generate/marker/<int:marker_id>")
    class MarkerGeneratorEndpoint(Resource):
        def get(self, marker_id):
            marker_data = MarkerRegistry().get_marker_for(marker_id)
            return send_file(BytesIO(marker_data), attachment_filename="marker{}.png".format(marker_id))

    @api.route("/detect/marker")
    class MarkerDetectorEndpoint(Resource):
        @api.expect(image_upload_parser)
        @api.marshal_with(markers_model)
        def post(self):
            args = image_upload_parser.parse_args()
            uploaded_file = args['file']
            stream = BytesIO()
            uploaded_file.save(stream)
            ids = MarkerDetector()(stream)
            
            return {'ids': list(ids)}

    # @api.route("/export/excel")
    # @api.route("/export/xls")
    # @api.route("/export/xlsx")
    # class ExcelExportEndpoint(Resource):
    #     def get(self):
    #         pass

    # @api.route("/export/web")
    # class ExcelExportEndpoint(Resource):
    #     def get(self):
    #         pass

    return app

def run_webserver(host:str, port:int, *a, **kw):
    api = setup_api()
    api.run(host=host, port=port, *a, **kw)
