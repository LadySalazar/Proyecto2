#!/usr/bin/python3
from modelo.producto import productoClass as pro
import cgi
import json
data=cgi.FieldStorage()
productos=pro.ObtenerProducto()
print('Content-Type:text/json')
print('')
print('[')
i=1
for producto in productos:
 print(json.dumps(producto.__dict__))
 if i<len(productos):
  i=i+1
  print(',')
print(']')

