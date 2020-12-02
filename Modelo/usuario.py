#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode

class usuarioClass:
 identificacion=None
 Nombre=None
 contrasenia=None
 correo=None
 def __init__(self,identificacion,Nombre,contrasenia,correo):
  self.identificacion=identificacion
  self.Nombre=Nombre
  self.contrasenia=contrasenia
  self.correo=correo

 def ObtenerUsuario():
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("select * from user")
   data = cursor.fetchall()
   if data == None:
    return None
   else:
    productos=[]
    for row in data:
     product=usuarioClass(identificacion=row[0],Nombre=row[1],contrasenia=row[2],correo=row[3])
     productos.append(product)
    return productos
   cursor.close()
  except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
   else:
    print(err)
  else:
   cnx.close()

 def ActualizarUsuario(id,nomb,contra,correo):
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("update user set Nombre='{}',contrasenia=sha('{}'),correo='{}' where Identificacion='{}'; ".format(nomb,contra,correo,id))
   cnx.commit()
   cursor.execute("select*from producto where Identificacion='{}' and Nombre='{}' and contrasenia=sha('{}') and correo='{}'; ".format(id,nomb,correo,contra))
   data = cursor.fetchall()
   if data == None:
    return False
   else:
    return True
   cursor.close()
  except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
   else:
    print(err)
  else:
   cnx.close()

 def crearUsuario(idC,nombreC,correoC,contraC):
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("insert into user (Identificacion,Nombre,contrasenia,correo) VALUE ('{}' ,'{}',sha('{}'),'{}'); ".format(idC,nombreC,correoC,contraC))
   cnx.commit()
   cursor.execute("select*from producto where Identificacion='{}' and Nombre='{}' and contrasenia=sha('{}') and correo='{}'; ".format(idC,nombreC,correoC,contraC))
   data = cursor.fetchall()
   if data == None:
    return False
   else:
    return True
   cursor.close()
  except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")

   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
   else:
    print(err)
  else:
   cnx.close()

 def BorrarUsuario(idC):
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("DELETE FROM user WHERE Identificacion='{}'".format(idC))
   cnx.commit()
   cursor.execute("select*from producto where Identificacion='{}'; ".format(idC))
   data = cursor.fetchall()
   if data == None:
    return False
   else:
    return True
   cursor.close()
  except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
   else:
    print(err)
  else:
   cnx.close()

