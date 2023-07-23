from tornado.web import RequestHandler

from db.setup import get_db

from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

def get_strategy():
    db = next(get_db())
    return Raw(db)

class SmokeTestHandler(RequestHandler):
    def get(self):
        self.write({"hello": "world"})

class GetHandler(RequestHandler):
    def get(self):
        results = get_strategy().all()
        self.write(results)
 
    def delete(self, pop_id):
        results = get_strategy().delete_by(int(pop_id))
        self.write(results)

class GetByFilterHandler(RequestHandler):
    def get(self, pop_id):
        results = get_strategy().filter_by(pop_id)
        self.write(results)

class InsertHandler(RequestHandler):
    def put(self, pop_name, pop_color):
        results = get_strategy().insert_entry(pop_name, pop_color)
        self.write(results)

class UpdateHandler(RequestHandler):
    def post(self, pop_id, pop_name, pop_color):
        results = get_strategy().update_entry(pop_id, pop_name, pop_color)
        self.write(results)
