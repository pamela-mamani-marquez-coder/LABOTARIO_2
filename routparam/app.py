from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nombre>")
def perfil_usuario(nombre):
    return f"Perfil de usuario: <strong>{nombre}</strong>"

@app.route("/post/<id>")
def ver_post(id):
    return f"Mostrando el Post: <strong>{id}</strong>"

@app.route("/categoria/<categoria>/<producto>")
def productos(categoria, producto):
    return f"Categoría: {categoria}, Producto: {producto}"
def ver_categoria(categoria, producto):
    return f"Mostrando la categoría: {categoria} con producto: {producto}"

if __name__ == "__main__":
    app.run(debug=True)