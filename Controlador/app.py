#!/usr/bin/python3
from modelo.producto import productoClass as pro
from modelo.usurio import usuarioClass as usu
from flask import Flask, request, jsonify
import json
app=Flask(__name__)
@app.route('/')
def hello():
  return "hello"

@app.route('/productos',methods=['POST'])
def productos():
  j=request.get_json()

  print(j.get('Aroma'))
  Creando=pro.crearProducto(j.get('id'),j.get('Aroma'),j.get('Imagen'),j.get('Nombre'),j.get('precio'),j.get('stock'),j.get('Tipo'))
  if Creando:
    return "True"
  else:
    return "False"

@app.route('/crearProductos',methods=['GET'])
def crearProductos():
  response_object = {'status': 'success'}
  productos=pro.ObtenerProducto()
  productorespuesta=[]
  for producto in productos:
   productorespuesta.append(producto.__dict__)

  response_object['produc'] = productorespuesta
  return jsonify(response_object)

@app.route('/actualizarProductos',methods=['PUT'])
def actualizarProductos():
  j=request.get_json()

  print(j.get('Aroma'))

  verif=pro.ActualizarProducto(j.get('id'),j.get('Aroma'),j.get('Imagen'),j.get('Nombre'),j.get('precio'),j.get('stock'),j.get('Tipo'))
  if verif:
    return "True"
  else:
    return "False"

@app.route('/borrarProductos',methods=['POST'])
def borrarProductos():
  j=request.get_json()
  delete=pro.BorrarProducto(j.get('ident'))
  if delete:
    return "True"
  else:
    return "False"

@app.route('/crearUsuarios',methods=['GET'])
def crearUsuarios():
  response_object = {'status': 'success'}
  productos=usu.ObtenerUsuario()
  productorespuesta=[]
  for producto in productos:
   productorespuesta.append(producto.__dict__)

  response_object['produc'] = productorespuesta
  return jsonify(response_object)

@app.route('/usuario',methods=['POST'])
def usuario():
  j=request.get_json()

  print(j.get('identificacion'))
  Creando=usu.crearUsuario(j.get('identificacion'),j.get('Nombre'),j.get('contrasenia'),j.get('correo'))
  if Creando:
    return "True"
  else:
    return "False"


@app.route('/actualizarUsuario',methods=['PUT'])
def actualizarUsuario():
  j=request.get_json()

  print(j.get('identificacion'))

  verif=usu.ActualizarUsuario(j.get('identificacion'),j.get('Nombre'),j.get('contrasenia'),j.get('correo'))
  if verif:
    return "True"
  else:
    return "False"


@app.route('/borrarUsuario',methods=['POST'])
def borrarUsuario():
  j=request.get_json()
  delete=usu.BorrarUsuario(j.get('ident'))
  if delete:
    return "True"
  else:
    return "False"



if __name__=='__main__':
  app.run(host="0.0.0.0")






