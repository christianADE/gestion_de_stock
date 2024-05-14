import pymysql.cursors
# Connexion a la base de donnee
CONNECTION = pymysql.connect(host='localhost',
                             user='python',
                             password='',
                             db='root',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)