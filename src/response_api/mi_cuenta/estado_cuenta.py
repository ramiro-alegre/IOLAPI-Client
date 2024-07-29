from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Estadistica:
    descripcion: str
    cantidad: int
    volumen: int

    @staticmethod
    def from_dict(obj: Any) -> 'Estadistica':
        _descripcion = str(obj.get("descripcion"))
        _cantidad = int(obj.get("cantidad"))
        _volumen = int(obj.get("volumen"))
        return Estadistica(_descripcion, _cantidad, _volumen)

@dataclass
class Saldo:
    liquidacion: str
    saldo: int
    comprometido: int
    disponible: int
    disponibleOperar: int

    @staticmethod
    def from_dict(obj: Any) -> 'Saldo':
        _liquidacion = str(obj.get("liquidacion"))
        _saldo = int(obj.get("saldo"))
        _comprometido = int(obj.get("comprometido"))
        _disponible = int(obj.get("disponible"))
        _disponibleOperar = int(obj.get("disponibleOperar"))
        return Saldo(_liquidacion, _saldo, _comprometido, _disponible, _disponibleOperar)

@dataclass
class Cuenta:
    numero: str
    tipo: str
    moneda: str
    disponible: int
    comprometido: int
    saldo: int
    titulosValorizados: int
    total: int
    margenDescubierto: int
    saldos: List[Saldo]
    estado: str

    @staticmethod
    def from_dict(obj: Any) -> 'Cuenta':
        _numero = str(obj.get("numero"))
        _tipo = str(obj.get("tipo"))
        _moneda = str(obj.get("moneda"))
        _disponible = int(obj.get("disponible"))
        _comprometido = int(obj.get("comprometido"))
        _saldo = int(obj.get("saldo"))
        _titulosValorizados = int(obj.get("titulosValorizados"))
        _total = int(obj.get("total"))
        _margenDescubierto = int(obj.get("margenDescubierto"))
        _saldos = [Saldo.from_dict(y) for y in obj.get("saldos")]
        _estado = str(obj.get("estado"))
        return Cuenta(_numero, _tipo, _moneda, _disponible, _comprometido, _saldo, _titulosValorizados, _total, _margenDescubierto, _saldos, _estado)

@dataclass
class EstadoCuenta:
    cuentas: List[Cuenta]
    estadisticas: List[Estadistica]
    totalEnPesos: int

    @staticmethod
    def from_dict(obj: Any) -> 'EstadoCuenta':
        _cuentas = [Cuenta.from_dict(y) for y in obj.get("cuentas")]
        _estadisticas = [Estadistica.from_dict(y) for y in obj.get("estadisticas")]
        _totalEnPesos = int(obj.get("totalEnPesos"))
        return EstadoCuenta(_cuentas, _estadisticas, _totalEnPesos)