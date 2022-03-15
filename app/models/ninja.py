from app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for n in results:
            ninjas.append(cls(n))
        return ninjas
    
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls, data):
        pass
    
    @classmethod
    def update(cls, data):
        pass
    
    @classmethod
    def delete(cls, data):
        pass