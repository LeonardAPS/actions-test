from sqlalchemy import create_engine
from conf import MysqlConfig

class MysqlDatabase():
    def __init__(self, databasename):
        self.databasename = databasename
        self._conf = MysqlConfig()

    def connect(self):
        return create_engine(
            "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                self._conf.user, self._conf.password, self._conf.host, self._conf.port, self.databasename
            )
        )
