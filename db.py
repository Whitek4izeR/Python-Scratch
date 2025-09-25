import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="crossover.proxy.rlwy.net",
        port=44374,                   
        user="root",        
        password="GZcaMrNzVXLjCASRjuvHUTjWgzkorhUI",  
        database="railway"                
    )
