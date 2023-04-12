from connector import MysqlDatabase
from conf import MysqlConfig

def main():
    x = MysqlConfig()
    print(x.host)
    print("HELLO")

if __name__ == '__main__':
    main()