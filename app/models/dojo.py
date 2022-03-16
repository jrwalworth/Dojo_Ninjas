from app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos=[]
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_all_ninjas_from_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id  where dojos.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query)
        dojo = cls(results[0])
        for db_row in results:
            ninja_data = {
                "id" : db_row["ninjas.id"],
                "first_name" : db_row["first_name"],
                "last_name" : db_row["last_name"],
                "age" : db_row["age"],
                "created_at" :  db_row["created_at"],
                "updated_at" : db_row["updated_at"]
            }
            dojo.ninjas.append((cls.db).Ninja(ninja_data))
        return dojo
    
    

    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() );"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

