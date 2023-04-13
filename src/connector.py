from conf import MysqlConfig,PostgresConfig,CallbiConfig,SftpConfig
from sqlalchemy import create_engine
import pysftp

class SFTP:
    def __init__(self):
        self._conf = SftpConfig()
 
    def connect(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None # disable host key checking
        return pysftp.Connection(host=self._conf.host, username=self._conf.user, password=self._conf.password ,port =5555 , cnopts=cnopts)







