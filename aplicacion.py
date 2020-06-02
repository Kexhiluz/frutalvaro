from flask import Flask, jsonify, request

app = Flask(__name__)

from frutas import productos

@app.route("/productos")
def obtenerProductos():
    return jsonify({"productos": productos, "mensaje": "Lista de frutas" })

@app.route("/productos/<string:nombre_producto>")
def obtenerProducto(nombre_producto):
    productos_encontrados = [productos for productos in productos if productos["ID"] == nombre_producto]
    if (len(productos_encontrados)) > 0:
        return jsonify({"producto": productos_encontrados[0]})
    return jsonify({"mensaje": "El producto no se ha encontrado"})

@app.route("/productos", methods=["POST"])
def añadirProducto():
    producto_nuevo = {
        "ID": request.json["ID"],
        "nombre": request.json["nombre"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"],
        "categoria": request.json["categoria"],
        "marca": request.json["marca"]
    }
    productos.append(producto_nuevo)
    return jsonify({"mensaje": "El producto ha sido agregado a la lista", "productos": productos})

@app.route("/products/<string:nombre_producto>", methods=["PUT"])
def editarProducto(nombre_producto):
    productos_encontrados = [productos for productos in productos if productos["ID"] == nombre_producto]
    if (len(productos_encontrados) > 0):
        productos_encontrados[0]["ID"] = request.json["ID"]
        productos_encontrados[0]["nombre"] = request.json["nombre"]
        productos_encontrados[0]["cantidad"] = request.json["cantidad"]
        productos_encontrados[0]["categoria"] = request.json["categoria"]
        productos_encontrados[0]["marca"] = request.json["marca"]
        return jsonify({
            "mensaje": "El producto ha sido actualizado",
            "producto": productos_encontrados[0]
        })
    return jsonify({"mensaje": "producto no encontrado"})

@app.route('/products/<string:nombre_producto>', methods=['DELETE'])
def borrarProducto(nombre_producto):
    for productos in productos:
        if productos['nombre']==nombre_producto.lower():
            productos_encontrados=productos

    if len(productos_encontrados)>0:
        productos.remove(productos_encontrados[0])
        return jsonify({
            'mensaje': 'El producto ha sido borrado',
            'productos': productos
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000)  