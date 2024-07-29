from typing import Any, List
from dataclasses import dataclass

@dataclass
class Operacion:
    numero: int
    fechaOrden: str
    tipo: str
    estado: str
    mercado: str
    simbolo: str
    cantidad: int
    monto: int
    modalidad: str
    precio: int
    fechaOperada: str
    cantidadOperada: int
    precioOperado: int
    montoOperado: int
    plazo: str

    @staticmethod
    def from_dict(obj: Any) -> 'Operacion':
        _numero = int(obj.get("numero")) if obj.get("numero") is not None else None
        _fechaOrden = str(obj.get("fechaOrden")) if obj.get("fechaOrden") is not None else None
        _tipo = str(obj.get("tipo")) if obj.get("tipo") is not None else None
        _estado = str(obj.get("estado")) if obj.get("estado") is not None else None
        _mercado = str(obj.get("mercado")) if obj.get("mercado") is not None else None
        _simbolo = str(obj.get("simbolo")) if obj.get("simbolo") is not None else None
        _cantidad = int(obj.get("cantidad")) if obj.get("cantidad") is not None else None
        _monto = int(obj.get("monto")) if obj.get("monto") is not None else None
        _modalidad = str(obj.get("modalidad")) if obj.get("modalidad") is not None else None
        _precio = int(obj.get("precio")) if obj.get("precio") is not None else None
        _fechaOperada = str(obj.get("fechaOperada")) if obj.get("fechaOperada") is not None else None
        _cantidadOperada = int(obj.get("cantidadOperada")) if obj.get("cantidadOperada") is not None else None
        _precioOperado = int(obj.get("precioOperado")) if obj.get("precioOperado") is not None else None
        _montoOperado = int(obj.get("montoOperado")) if obj.get("montoOperado") is not None else None
        _plazo = str(obj.get("plazo")) if obj.get("plazo") is not None else None
        return Operacion(_numero, _fechaOrden, _tipo, _estado, _mercado, _simbolo, _cantidad, _monto, _modalidad, _precio, _fechaOperada, _cantidadOperada, _precioOperado, _montoOperado, _plazo)

@dataclass
class Operaciones:
    operaciones: List[Operacion]

    @staticmethod
    def from_dict(obj: Any) -> 'Operaciones':
        _operaciones =  [Operacion.from_dict(y) for y in obj]
        return Operaciones(_operaciones)