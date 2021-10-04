# TODO handle interaction between view and database 
# handle configuration of db query info
# should be able to make queries to any db type - sql, mysql, api, sqlite, etc

class ViewModel:

    def __init__(self, db):
        self.db = db
    
    def get_topics(self):
        return self.db.get_topics()
    
    def get_questions(self, topic):
        return self.db.get_questions(topic)
    
    def add_result(self, result):
        self.db.add_result(result)
    
    def show_results(self, user_id):
        return self.db.show_results(user_id)
