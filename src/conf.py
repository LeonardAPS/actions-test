import os

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