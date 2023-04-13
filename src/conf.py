import os

class MysqlConfig():
    @property
    def host(self):
        return os.environ["MYSQL_HOST"]
    
    @property
    def user(self):
        return os.environ["MYSQL_USER"]

    @property
    def password(self):
        return os.environ["MYSQL_PASS"]

    @property
    def port(self):
        return os.environ["MYSQL_PORT"]
        
class PostgresConfig():
    @property
    def host(self):
        return os.environ["POSTGRES_HOST"]
    
    @property
    def user(self):
        return os.environ["POSTGRES_USER"]

    @property
    def password(self):
        return os.environ["POSTGRES_PASS"]

    @property
    def port(self):
        return os.environ["POSTGRES_PORT"]

class SftpConfig():
    @property
    def host(self):
        return os.environ["SFTP_HOST"]
    
    @property
    def user(self):
        return os.environ["SFTP_USER"]

    @property
    def password(self):
        return os.environ["SFTP_PASS"]

    @property
    def port(self):
        return os.environ["SFTP_PORT"]

class CallbiConfig():
    @property
    def api_key(self):
        return os.environ["CALLBI_KEY"]

    @property
    def organization_key(self):
        return os.environ["CALLBI_ORG"]