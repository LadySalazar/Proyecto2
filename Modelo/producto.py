#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode

class productoClass:
 idProducto=None
 imagen=None
 nombre=None
 TipoProducto=None
 aroma=None
 precio=None
 Cantida =None
 def __init__(self,idProducto,imagen,nombre,TipoProducto,aroma,precio,Cantidad):
  self.idProducto=idProducto
  self.imagen=imagen
  self.nombre=nombre
  self.TipoProducto=TipoProducto
  self.aroma=aroma
  self.precio=precio
  self.Cantidad=Cantidad

 def ObtenerProducto():
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("select * from producto")
   data = cursor.fetchall()
   if data == None:
    return None
   else:
    productos=[]
    for row in data:
     product=productoClass(idProducto=row[0],imagen=row[1],nombre=row[2],TipoProducto=row[3],aroma=row[4],precio=row[5],Cantidad=row[6])
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

 def ActualizarProducto(id,arom,img,nomb,prec,cant,tipoP):
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("update producto set imagen='{}' ,nombre='{}',TipoProducto='{}',aroma='{}',precio='{}',Cantidad='{}' where idProducto='{}'; ".format(img,nomb,tipoP,arom,prec,cant,id))
   cnx.commit()
   cursor.execute("select*from producto where imagen='{}' and nombre='{}' and TipoProducto='{}' and aroma='{}' and precio='{}'and Cantidad='{}' and idProducto='{}'; ".format(img,nomb,tipoP,arom,prec,cant,id))
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

 def crearProducto(idC,aromC,imgC,nombC,precC,cantC,tipoPC):
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("insert into producto (imagen,nombre,TipoProducto,aroma,precio,Cantidad,idProducto) VALUE ('{}' ,'{}','{}','{}','{}','{}','{}'); ".format(imgC,nombC,tipoPC,aromC,precC,cantC,idC))
   cnx.commit()
   cursor.execute("select*from producto where imagen='{}' and nombre='{}' and TipoProducto='{}' and aroma='{}' and precio='{}'and Cantidad='{}' and idProducto='{}'; ".format(imgC,nombC,tipoPC,aromC,precC,cantC,idC))
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

 def BorrarProducto(idC):
  try:
   cnx = mysql.connector.connect(user='username', password = 'Lady@1234', database='DataBaseArquitectura',host='127.0.0.1')
   cursor = cnx.cursor()
   cursor.execute("DELETE FROM producto WHERE idProducto='{}'".format(idC))
   cnx.commit()
   cursor.execute("select*from producto where idProducto='{}'; ".format(idC))
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



