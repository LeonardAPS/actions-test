import os

class MysqlConfig():
    @property
    def host(self):
        return "YAY"
    
    @property
    def user(self):
        return os.environ["MYSQL_USER"]

    @property
    def password(self):
        return os.environ["MYSQL_PASSWORD"]

    @property
    def port(self):
        return os.environ["MYSQL_PORT"]
    



# os.environ["MYSQL_HOST"]