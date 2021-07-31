from flask import Flask, jsonify, request
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import random as r
from datetime import date, datetime, timedelta
from sqlalchemy.orm import session
from sqlalchemy.sql.schema import BLANK_SCHEMA

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Perrogta1@localhost:5432/tarea3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

now = datetime.now()

#  A continuacion hay codigo que genera datos en una base de datos que no posea ninguno
# en caso de que ya hayan datos no deberian de insertarse mas datos

paises = [
    (1, 'Angola'),
    (2, 'Sudáfrica'),
    (3, 'Canadá'),
    (4, 'Estados Unidos'),
    (5, 'Chile'),
    (6, 'Australia'),
    (7, 'India'),
    (8, 'Corea del Sur'),
    (9, 'Rusia'),
    (10, 'Suiza'),
    (11, 'Sin pais')]

# Clase en la que se crea la tabla de los paises


class Country(db.Model):
    __tablename__ = 'pais'
    cod_pais = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __init__(self, cod_pais, nombre):
        self.cod_pais = cod_pais
        self.nombre = nombre

    def json(self):
        return {
            'cod_pais': self.cod_pais,
            'nombre': self.nombre
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()


try:
    for i in range(len(paises)):
        country = Country(paises[i][0], paises[i][1])
        db.session.add(country)
        db.session.commit()
    print("--Paises agregados")
except:
    print("++Ya habian paises generados")


def generateFecha():
    y = r.randint(2015, 2019)
    m = r.randint(1, 12)
    d = r.randint(1, 31)
    if m in [4, 6, 9, 11] and d > 30:
        d = 30
    if m == 2 and d > 28:
        d = 28
    return datetime(y, m, d)


usuarios = [
    (1, 'Carlos', 'Matos',      'carlos.matos@bitconnect.com',
     '68B826DEFEB8A', r.randint(1, 10), generateFecha()),
    (2, 'Kaidan', 'Jones',      'kaidan.jones@gmail.com',
     'FF5506AAEF96E', r.randint(1, 10), generateFecha()),
    (3, 'Dimitri', 'Knights',   'dimitri.knights@yahoo.com',
     '4F44213796B1D', r.randint(1, 10), generateFecha()),
    (4, 'Seb', 'Cope',          'seb.cope@hotmail.com',
     'CD6CAE1FB5D66', r.randint(1, 10), generateFecha()),
    (5, 'Bella', 'Hamilton',    'bella.hamilton@outlook.com',
     'EFF0728386589', r.randint(1, 10), generateFecha()),
    (6, 'Khadijah', 'Briggs',   'khadijah.briggs@msn.com',
     'EE021DC005AA8', r.randint(1, 10), generateFecha()),
    (7, 'Marcelo', 'Panire',    'marcelo.panire@gmail.com',
     '3C90FB8FB6706', r.randint(1, 10), generateFecha()),
    (8, 'Shola', 'Shea',        'shola.shea@msn.com',
     '97F3C78AFF2C2', r.randint(1, 10), generateFecha()),
    (9, 'Dayna', 'Mcclain',     'dayna.mcclain@gmail.com',
     'FA129A29CAAD1', r.randint(1, 10), generateFecha()),
    (10, 'Henri', 'Wicks',      'henri.wicks@hotmail.com',
     '2E6A1C9F2EC14', r.randint(1, 10), generateFecha()),
    (11, 'Willow', 'Fuller',    'willow.fuller@yahoo.com',
     'DD52CC4FB60C0', r.randint(1, 10), generateFecha()),
    (12, 'Odin', 'Lopez',       'odin.lopez@hotmail.com',
     '964A6E2DF2A28', r.randint(1, 10), generateFecha()),
    (13, 'Aqeel', 'Blundell',   'aqeel.blundell@outlook.com',
     'C80351F8FC04B', r.randint(1, 10), generateFecha()),
    (14, 'Cecilia', 'Reyes',    'cecilia.reyes@gmail.com',
     '76664E4E3637F', r.randint(1, 10), generateFecha()),
    (15, 'Evelyn', 'Pratt',     'evelyn.pratt@msn.com',
     'F979701816EA2', r.randint(1, 10), generateFecha()),
    (16, 'Gloria', 'Connelly',  'gloria.connelly@yahoo.com',
     '5878D12E78D97', r.randint(1, 10), generateFecha()),
    (17, 'Samanta', 'Carter',   'samanta.carter@hotmail.com',
     '1BE8678AA0A45', r.randint(1, 10), generateFecha()),
    (18, 'Gracie-May', 'Beech', 'graciemay.beech@outlook.com',
     'B22D3AA428B9B', r.randint(1, 10), generateFecha()),
    (19, 'Ferne', 'Norman',     'ferne.norman@gmail.com',
     'DCA2A015216B1', r.randint(1, 10), generateFecha()),
    (20, 'Kimberly', 'Richard', 'kimberly.richard@gmail.com',
     '31C332158A7A0', r.randint(1, 10), generateFecha()),
    (21, 'Anwar', 'Bains',      'anwar.bains@outlook.com',
     '75946A836400B', r.randint(1, 10), generateFecha()),
    (22, 'Reon', 'Mcneil',      'reon.mcneil@gmail.com',
     '446B6ACE57698', r.randint(1, 10), generateFecha()),
    (23, 'Saqib', 'Andrews',    'saqib.andrews@yahoo.com',
     '8D367BB2B2DA3', r.randint(1, 10), generateFecha()),
    (24, 'Elif', 'Floyd',       'elif.floyd@hotmail.com',
     '7E69A5468DE22', r.randint(1, 10), generateFecha()),
    (25, 'Mai', 'Duffy',        'mai.duffy@yahoo.com',
     'C75F04A1B176C', r.randint(1, 10), generateFecha())]
# Clase en la que se crea la tabla de los usuarios


class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.Integer,  db.ForeignKey('pais.cod_pais'))
    fecha_registro = db.Column(db.DateTime, nullable=False)

    def __init__(self, id,  nombre, apellido, correo, contrasena, pais, time):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.pais = pais
        self.fecha_registro = time

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'contrasena': self.contrasena,
            'pais': self.pais,
            'fecha_registro': self.fecha_registro
        }


try:
    for i in range(len(usuarios)):
        usuario = User(usuarios[i][0], usuarios[i][1], usuarios[i][2],
                       usuarios[i][3], usuarios[i][4], usuarios[i][5], usuarios[i][6])
        db.session.add(usuario)
        db.session.commit()
    print("--Usuarios de prueba generados")
except:
    print("++Ya habian usuarios generados")

monedas = [
    (1, 'BTC', 'Bitcoin'),
    (2, 'ETH', 'Ethereum'),
    (3, 'LTC', 'Litecoin'),
    (4, 'DOGE', 'Dogecoin'),
    (5, 'USDT', 'Tether USD'),
    (6, 'XLM', 'Stellar Lumens'),
    (7, 'XRP', 'Ripple'),
    (8, 'BCC', 'Bitconnect'),
    (9, 'DRCY', 'Prestigiocoin'),
    (10, 'RP', 'Riot Points')]
# Clase en la que se crea la tabla de las monedas


class Coin(db.Model):
    __tablename__ = 'moneda'
    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String(10), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)

    def __init__(self, id, sigla, nombre):
        self.id = id
        self.sigla = sigla
        self.nombre = nombre

    def json(self):
        return {
            'id': self.id,
            'sigla': self.sigla,
            'nombre': self.nombre
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()


try:
    for i in range(len(monedas)):
        coin = Coin(monedas[i][0], monedas[i][1], monedas[i][2])
        db.session.add(coin)
        db.session.commit()
    print("--Se han generado las monedas")
except:
    print("++Ya hay datos de monedas existentes en la Base de datos")

# precio_moneda
precios_monedas = []
for idMoneda in range(1, 11):
    n_cambios = r.randint(5, 25)
    to_add = []
    for i in range(n_cambios):
        td = timedelta(
            weeks=r.randint(0, 51),
            days=r.randint(0, 6),
            hours=r.randint(0, 23),
            minutes=r.randint(0, 59),
            seconds=r.randint(0, 59)
        )
        to_add.append((idMoneda, now - td, r.randint(1, 10000)/10))
    to_add.sort()
    precios_monedas = precios_monedas + to_add
# Clase en la que se crea la tabla de los precios de las monedas


class Coin_price(db.Model):
    __tablename__ = 'precio_moneda'
    id_moneda = db.Column(db.Integer, db.ForeignKey('moneda.id'))
    fecha = db.Column(db.DateTime, primary_key=True)
    valor = db.Column(db.Float, nullable=False)

    def __init__(self, id_moneda, fecha, valor):
        self.id_moneda = id_moneda
        self.fecha = fecha
        self.valor = valor

    def json(self):
        return {
            'id_moneda': self.id_moneda,
            'fecha': self.fecha,
            'valor': self.valor
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()


try:
    for i in range(len(precios_monedas)):
        sus = Coin_price(
            precios_monedas[i][0], precios_monedas[i][1], precios_monedas[i][2])
        db.session.add(sus)
        db.session.commit()
    print("--Se le ha dado valor a las monedas")
except:
    print("++Las monedas poseian valor de antes")

cuentas_bancarias = [(1, 1, 0.01)]
usuario_tiene_moneda = [(1, 8, round(r.uniform(70.0, 100.0), 2))]
options = [i for i in range(1, 11)]
N_CTA = 2
for i in range(2, 26):
    n_ctas = r.randint(0, 3)
    to_add = []
    for j in range(n_ctas):
        to_add.append((N_CTA, i, round(r.uniform(0.0, 10000.0), 2)))
        N_CTA = N_CTA + 1
    cuentas_bancarias = cuentas_bancarias + to_add
    n_monedas = r.randint(0, 3)
    m = r.sample(options, k=n_monedas)
    for j in m:
        usuario_tiene_moneda.append((i, j, round(r.uniform(0.0, 100.0), 2)))
# Clase en la que se crea la tabla de las monedas que posee un usuario


class User_have_coin(db.Model):
    __tablename__ = 'usuario_tiene_moneda'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_moneda = db.Column(db.Integer, db.ForeignKey('moneda.id'))
    balance = db.Column(db.Float, nullable=False)
    primary = db.Column(db.Integer, primary_key=True)

    def __init__(self, id_usuario, id_moneda, balance, primary):
        self.id_usuario = id_usuario
        self.id_moneda = id_moneda
        self.balance = balance
        self.primary = primary

    def json(self):
        return {
            'id_usuario': self.id_usuario,
            'id_moneda': self.id_moneda,
            'balance': self.balance,
            'primary': self.primary
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()


try:
    for i in range(len(usuario_tiene_moneda)):
        si = User_have_coin(
            usuario_tiene_moneda[i][0], usuario_tiene_moneda[i][1], usuario_tiene_moneda[i][2], i)
        db.session.add(si)
        db.session.commit()
    print("--Datos de que monedas tiene un usuario de prueba genereados")
except:
    print("++Los usuarios de prueba ya poseian monedas de antes")
# Clase en la que se crea la tabla de las cuentas bancarias


class BankA(db.Model):
    __tablename__ = 'cuenta_bancaria'
    numero_cuenta = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, numero_cuenta, id_usuario, balance):
        self.numero_cuenta = numero_cuenta
        self.id_usuario = id_usuario
        self.balance = balance

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def json(self):
        return {
            'numero_cuenta': self.numero_cuenta,
            'id_usuario': self.id_usuario,
            'balance': self.balance
        }

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False


try:
    for i in range(len(cuentas_bancarias)):
        account = BankA(
            cuentas_bancarias[i][0], cuentas_bancarias[i][1], cuentas_bancarias[i][2])
        db.session.add(account)
        db.session.commit()
    print("--Cuentas bancarias de prueba generadas")
except:
    print('++Ya habian cuentas bancarias de prueba generadas')

db.create_all()


@app.route('/task', methods=['GET'])
def create_user():
    return 'recibido'
##############################################


# Añadir un usuario
@app.route("/api/usuario", methods=['POST'])
def addUser():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    pais = request.json['pais']
    now = datetime.now()
    last = User.query.order_by(User.id.desc())
    first = last.first()
    new_user = User((first.id + 1), nombre, apellido,
                    correo, contrasena, pais, now)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'user': new_user.json()})


# Obtener todos los usuarios
@app.route('/api/usuario', methods=['GET'])
def getUsers():
    users = [user.json() for user in User.query.all()]
    return jsonify({'users': users})


# Obtener un solo usuario
@app.route('/api/usuario/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'El usuario no existe'}), 404
    return jsonify({'user': user.json()})


# Actualizar un usuario
@app.route('/api/usuario/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'El usuario no existe'}), 404
    json = request.get_json(force=True)
    if json.get('nombre') is None:
        return jsonify({'message': 'Solicitud Incorrecta'}), 400
    user.nombre = request.json['nombre']
    user.apellido = request.json['apellido']
    user.correo = request.json['correo']
    user.contrasena = request.json['contrasena']
    user.pais = request.json['pais']
    user.update()
    return jsonify({'user': user.json()})


# Eliminar un usario
@app.route('/api/usuario/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'El usuario no existe'}), 404
    have = User_have_coin.query.filter_by(id_usuario=id).all()
    for i in range(len(have)):
        have[i].delete()
    bank = BankA.query.filter_by(id_usuario=id).all()
    for i in range(len(bank)):
        bank[i].delete()
    user.delete()
    return jsonify({'user': user.json()})

########################################################################

# Crear un pais nuevo
@app.route('/api/pais', methods=['POST'])
def createCountry():
    nombre = request['nombre']
    last = Country.query.order_by(User.id.desc())
    first = last.first()
    new_user = Country((first.id + 1), nombre)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'Pais creado': new_user.json()})


# Obtener todos los paises
@app.route('/api/pais', methods=['GET'])
def getCountries():
    countri = [country.json() for country in Country.query.all()]
    return jsonify({'users': countri})


# Obtener un pais en especifico
@app.route('/api/pais/<id>', methods=['GET'])
def getCountry(id):
    country = Country.query.filter_by(cod_pais=id).first()
    if country is None:
        return jsonify({'message': 'El pais no existe'}), 404
    return jsonify({'nombre': country.json()})


# Actualizar a un pais
@app.route('/api/pais/<id>', methods=['PUT'])
def updateCountry(id):
    country = Country.query.filter_by(cod_pais=id).first()
    if country is None:
        return jsonify({'message': 'No existe ese pais'})
    country.nombre = request.json['nombre']
    country.update()
    return jsonify({'Pais modificado': country.json()})


# Eliminar un pais
@app.route('/api/pais/<id>', methods=['DELETE'])
def delteCountry(id):
    country = Country.query.filter_by(cod_pais=id).first()
    user = User.query.filter_by(country=id).all()
    for i in range(len(user)):
        user[i].country = 11
        user[i].update()
    country.delete()
    return jsonify({'Pais eliminado': country.json()})

##########################################################################

# Agregar una cuenta bancaria
@app.route('/api/cuenta_bancaria', methods=['POST'])
def addBank():
    id_usuario = request.json['id_usuario']
    balance = request.json['balance']
    lista = BankA.query.order_by(BankA.numero_cuenta.desc())
    first = lista.first()
    new = BankA((first.numero_cuenta + 1), id_usuario, balance)
    db.session.add(new)
    db.session.commit()
    return jsonify({'id_usuario': new.json()})


# Obtener todas las cuentas bancarias
@app.route('/api/cuenta_bancaria', methods=['GET'])
def getBanks():
    bank = [banco.json() for banco in BankA.query.all()]
    return jsonify({'users': bank})


# Obtener una cuenta bancaria en especifica
@app.route('/api/cuenta_bancaria/<id>', methods=['GET'])
def getBank(id):
    bank = BankA.query.filter_by(numero_cuenta=id).first()
    if bank is None:
        return jsonify({'message': 'La cuenta bancaria no existe'}), 404
    return jsonify({'nombre': bank.json()})


# Actualizar una cuenta bancaria en especifico
@app.route('/api/cuenta_bancaria/<id>', methods=['PUT'])
def updateBank(id):
    banc = BankA.query.filter_by(numero_cuenta=id).first()
    if banc is None:
        return jsonify({'message': 'La cuenta bancaria no existe'}), 404
    banc.balance = request.json['balance']
    banc.update()
    return jsonify({'numero_cuenta': banc.json()})


# Eliminar una cuenta bancaria
@app.route('/api/cuenta_bancaria/<id>', methods=['DELETE'])
def deleteBank(id):
    user = BankA.query.filter_by(numero_cuenta=id).first()
    if user is None:
        return jsonify({'message': 'La cuenta bancaria no existe'}), 404
    user.delete()
    return jsonify({'message': 'La cuenta bancaria ha sido eliminada', 'user': user.json()})

##########################################################################

# Darle moenas a una persona
@app.route('/api/usuario_tiene_moneda/<id>', methods=['POST'])
def giveCoin(id):
    coin = User_have_coin.query.filter_by(id_usuario=id).first()
    if coin is None:
        return jsonify({'message': 'El usuario no existe'})
    coin.id_moneda = request.json['id_moneda']
    coin.balance = request.json['balance']
    last = User_have_coin.query.order_by(User_have_coin.primary.desc())
    first = last.first()
    coin.primary = first.primary + 1
    coin.update()
    return jsonify({'monedas dadas': coin.json()})


# Obtener las monedas que poseen los usuarios
@app.route('/api/usuario_tiene_moneda/', methods=['GET'])
def getMoneyUsers():
    coin = [moneda.json() for moneda in User_have_coin.query.all()]
    return jsonify({'Datos': coin})


# Obtener una moneda en especifico que posee un usuario
@app.route('/api/usuario_tiene_moneda/<id>/<coin>', methods=['GET'])
def getMoneyU(id, coin):
    bank = User_have_coin.query.filter(
        User_have_coin.id_usuario == id, User_have_coin.id_moneda == coin).first()
    if bank is None:
        return jsonify({'message': 'El usuario no posee esa monedas'}), 404
    return jsonify({'Datos': bank.json()})


# Actualizar una moneda que posee un usuario
@app.route('/api/usuario_tiene_moneda/<id>/<coin>', methods=['PUT'])
def updateUC(id, coin):
    banc = User_have_coin.query.filter(
        User_have_coin.id_usuario == id, User_have_coin.id_moneda == coin).first()
    if banc is None:
        return jsonify({'message': 'El usuario no posee esa moneda'}), 404
    banc.balance = request.json['balance']
    banc.update()
    return jsonify({'Datos actualizados': banc.json()})


# Eliminar las monedas que posee un usuario
@app.route('/api/usuario_tiene_moneda/<id>/<coin>', methods=['DELETE'])
def deleteUC(id, coin):
    user = User_have_coin.query.filter(
        User_have_coin.id_usuario == id, User_have_coin.id_moneda == coin).first()
    if user is None:
        return jsonify({'message': 'La moneda en ese usuario no existe'}), 404
    user.delete()
    return jsonify({'message': 'Las monedas del usuario han sido eliminadas', 'Datos': user.json()})

#######################################################################

# Crear una moneda nueva
@app.route('/api/moneda', methods=['POST'])
def createCoin():
    nombre = request.json['nombre']
    siglas = request.json['sigla']
    lista = Coin.query.order_by(Coin.id.desc())
    first = lista.first()
    new = Coin((first.id + 1), siglas, nombre)
    db.session.add(new)
    db.session.commit()
    return jsonify({'Moneda creada': new.json()})


# Obtener todas las monedas
@app.route('/api/moneda', methods=['GET'])
def getCoins():
    coin = [moneda.json() for moneda in Coin.query.all()]
    return jsonify({'Datos': coin})


# Obtener una moneda en especifico
@app.route('/api/moneda/<id>', methods=['GET'])
def getCoin(id):
    coin = Coin.query.filter_by(id=id).first()
    if coin is None:
        return jsonify({'message': 'El usuario no existe'}), 404
    return jsonify({'Moneda': coin.json()})


# Modificar una moneda
@app.route('/api/moneda/<id>', methods=['PUT'])
def updateCoin(id):
    coin = Coin.query.filter_by(numero_cuenta=id).first()
    if coin is None:
        return jsonify({'message': 'La moneda no existe'}), 404
    coin.nombre = request.json['nombre']
    coin.sigla = request.json['sigla']
    coin.update()
    return jsonify({'Moneda modifica': coin.json()})


# Eliminar una moneda
@app.route('/api/moneda/<id>', methods=['DELETE'])
def deleteCoin(id):
    coin = Coin.query.filter_by(id=id).first()
    if coin is None:
        return jsonify({'message': 'La moneda no existe'}), 404
    have = User_have_coin.query.filter_by(id_moneda=id).all()
    for i in range(len(have)):
        have[i].delete()
    price = Coin_price.query.filter_by(id_moneda=id).all()
    for i in range(len(price)):
        price[i].delete()
    coin.delete()
    return jsonify({'Moneda eliminada': coin.json()})

####################################################################

# Crear nuevo precio de una moneda
@app.route('/api/precio_moneda', methods=['POST'])
def newPrice():
    id_moneda = request.json['id_moneda']
    valor = request.json['valor']
    now = datetime.now()
    new_user = Coin_price(id_moneda, now, valor)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'Precio creado': new_user.json()})


# Obtener todos los valores que han tomado las monedas
@app.route('/api/precio_moneda', methods=['GET'])
def getPrices():
    price = [coin.json() for coin in Coin_price.query.all()]
    return jsonify({'Datos': price})


# Obtener la ultima modificacion del precio de una moneda
@app.route('/api/precio_moneda/<id>', methods=['GET'])
def getPrice(id):
    coin = Coin_price.query.filter_by(id_moneda=id).first()
    if coin is None:
        return jsonify({'message': 'El usuario no existe'}), 404
    lista = coin.query.order_by(Coin_price.fecha.desc()).first()
    return jsonify({'Moneda': lista.json()})


# Modificar precio que ha tenido una moneda (Esta solicitud no funciona)
@app.route('/api/precio_moneda/<id>/<ano>/<mes>/<dia>', methods=['PUT'])
def updatePrice(id, ano, mes, dia):
    date = datetime(int(ano), int(mes), int(dia))
    coin = Coin_price.query.filter(
        str(Coin_price.fecha)[0:4] == date, Coin_price.id_moneda == id).first()
    print(date.year)
    if coin is None:
        return jsonify({'message': 'La moneda en esa fecha no existe'}), 404
    coin.price = request.json['valor']
    coin.update()
    return jsonify({'message': 'el precio ha sido eliminado', 'Datos': coin.json()})


# Eliminar un dato  (Esta solicitud no funciona)
@app.route('/api/precio_moneda/<id>/<ano>/<mes>/<dia>', methods=['DELETE'])
def deletePrice(id, ano, mes, dia):
    coin = Coin_price.query.filter(Coin_price.fecha == date)
    sql = db.session.execute(text(" DELETE FROM precio_moneda WHERE SUBSTRING(cast(fecha as varchar(100)),1, 4) = :ano and SUBSTRING(cast(fecha as varchar(100)),6,7) = :mes and SUBSTRING(cast(fecha as varchar(100)),9, 10) = :dia and id_moneda = :id"),{'ano':ano, 'mes':mes,'dia':dia, 'id':id})
    a = []
    datee = str(ano) +"-"+ str(mes)+"-"+ str(dia)
    print(sql)
    a.append(datee)
    a.append(id)
    json_file= json.dumps(a)
    return jsonify({'Fecha / ID': json_file})

# C O N S U L T A S

@app.route('/api/consulta1/<year>', methods=['GET'])  # no funciona aun
def Consulta1(year):
    try:
        result = db.session.execute(text("SELECT nombre , apellido, id , SUBSTRING(cast(fecha_registro as varchar(100)),1, 10) FROM usuario WHERE SUBSTRING(cast(fecha_registro as varchar(100)),1, 4) = :year"), {'year': year})
        test = result.all()
        a = []
        print(result)
        for i in range(len(test)):
            c=[]
            c.append(test[i][0])
            c.append(test[i][1])
            c.append(test[i][2])
            c.append(test[i][3])
            a.append(c)
        json_file= json.dumps(a)
        return jsonify({'Nombre / Apellido / ID / Fecha': json_file})
    except Exception as e:
        return jsonify({'message': e })

@app.route('/api/consulta2/<value>', methods=['GET'])
def Consulta2(value):
    acc = BankA.query.filter(BankA.balance > value).all()
    a = []
    for i in range(len(acc)):
        c = []
        c.append(acc[i].numero_cuenta)
        c.append(acc[i].balance)
        a.append(c)
    if acc is None:
        return jsonify({'message': 'No hay cuenta bancaria con una balance super a ese'}), 404
    json_data = json.dumps(a)
    return jsonify({'Numero de cuenta / Balance': json_data})


@app.route('/api/consulta3/<country>', methods=['GET'])
def Consulta3(country):
    pais = Country.query.filter(Country.nombre == country).first()
    user = User.query.filter(User.pais == pais.cod_pais).all()
    a = []
    for i in range(len(user)):
        c = []
        c.append(user[i].nombre)
        c.append(user[i].apellido)
        c.append(user[i].id)
        a.append(c)
    if user is None:
        return jsonify({'message': 'No hay gente en el pais especificado'}), 404
    json_data = json.dumps(a)
    return jsonify({'Nombre / Apellido / ID': json_data})


@app.route('/api/consulta4/<coin>', methods=['GET'])
def Consulta4(coin):
    si = Coin.query.filter(Coin.nombre == coin).first()
    if si is None:
        return jsonify({'message': 'No se encontro moneda'}), 404
    coin = Coin_price.query.filter(si.id == Coin_price.id_moneda).order_by(
        Coin_price.valor.desc()).first()
    return jsonify({'Fecha / ID moneda / Valor': coin.json()})


@app.route('/api/consulta5/<coin>', methods=['GET'])
def Consulta5(coin):
    si = Coin.query.filter(Coin.nombre == coin).first()
    if si is None:
        return jsonify({'message': 'No se encontro moneda'}), 404
    coin = Coin_price.query.filter(si.id == Coin_price.id_moneda).all()
    total = 0
    for i in range(len(coin)):
        total = total + (coin[i].valor)
    json_data = json.dumps(total)
    return jsonify({'Valor': json_data})


if (__name__ == '__main__'):
    app.run(debug=True, port=6969)
