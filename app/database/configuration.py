#Datos conexion base de datos
userName ="root"
userPassword = ""
connectionPort = 3306
dataBaseName = "gesrtordb"
server="localhost"

#crear conexion
dataBaseConnection=f"msql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)