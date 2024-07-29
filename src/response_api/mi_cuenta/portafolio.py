from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Parking:
    disponibleInmediato: int

    @staticmethod
    def from_dict(obj: Any) -> 'Parking':
        _disponibleInmediato = int(obj.get("disponibleInmediato"))
        return Parking(_disponibleInmediato)

@dataclass
class Titulo:
    simbolo: str
    descripcion: str
    pais: str
    mercado: str
    tipo: str
    plazo: str
    moneda: str

    @staticmethod
    def from_dict(obj: Any) -> 'Titulo':
        _simbolo = str(obj.get("simbolo"))
        _descripcion = str(obj.get("descripcion"))
        _pais = str(obj.get("pais"))
        _mercado = str(obj.get("mercado"))
        _tipo = str(obj.get("tipo"))
        _plazo = str(obj.get("plazo"))
        _moneda = str(obj.get("moneda"))
        return Titulo(_simbolo, _descripcion, _pais, _mercado, _tipo, _plazo, _moneda)

@dataclass
class Activo:
    cantidad: int
    comprometido: int
    puntosVariacion: int
    variacionDiaria: int
    ultimoPrecio: int
    ppc: int
    gananciaPorcentaje: int
    gananciaDinero: int
    valorizado: int
    titulo: Titulo
    parking: Parking

    @staticmethod
    def from_dict(obj: Any) -> 'Activo':
        _cantidad = int(obj.get("cantidad"))
        _comprometido = int(obj.get("comprometido"))
        _puntosVariacion = int(obj.get("puntosVariacion"))
        _variacionDiaria = int(obj.get("variacionDiaria"))
        _ultimoPrecio = int(obj.get("ultimoPrecio"))
        _ppc = int(obj.get("ppc"))
        _gananciaPorcentaje = int(obj.get("gananciaPorcentaje"))
        _gananciaDinero = int(obj.get("gananciaDinero"))
        _valorizado = int(obj.get("valorizado"))
        _titulo = Titulo.from_dict(obj.get("titulo"))
        _parking = Parking.from_dict(obj.get("parking")) if obj.get("parking") is not None else None
        return Activo(_cantidad, _comprometido, _puntosVariacion, _variacionDiaria, _ultimoPrecio, _ppc, _gananciaPorcentaje, _gananciaDinero, _valorizado, _titulo, _parking)

@dataclass
class Portafolio:
    pais: str
    activos: List[Activo]

    @staticmethod
    def from_dict(obj: Any) -> 'Portafolio':
        _pais = str(obj.get("pais"))
        _activos = [Activo.from_dict(y) for y in obj.get("activos")]
        return Portafolio(_pais, _activos)