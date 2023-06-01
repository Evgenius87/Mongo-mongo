from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASS')
db_name = config.get('DB', 'DB_NAME')


connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{db_name}.0t39yjj.mongodb.net/?retryWrites=true&w=majority""", ssl=True)

