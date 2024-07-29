# IOLAPI-Client

Este repositorio tiene como objetivo dar una base para utilizar la API v2 de [IOL](https://www.invertironline.com/).

## Uso

Para uso local, es conveniente instalar python-dotenv

```python
pip install python-dotenv
```

Crear entorno

```python
python -m venv IOLApi-Client-venv
```

Activar entorno (En windows)

```python
IOLApi-Client-venv\Scripts\activate.bat
```

Instalar dependencias

```python
pip install -r requirements.txt
```

### Código

#### Obtener saldo actual de cuenta argentina

```python
from IOLApi import IOLApi
import asyncio

async def main():
    iol = IOLApi()
    await iol.login(
        username='', # Correo electronico
        password=''
    )

    estado_cuenta = await iol.get_estadocuenta()
    cuenta_arg = [cuenta for cuenta in estado_cuenta.cuentas if cuenta.moneda == 'peso_Argentino'][0]
    print(cuenta_arg.saldo)

if __name__ == '__main__':
    asyncio.run(main=main())
```

#### Obtener cantidad de activos especificos en una cuenta

```python
from IOLApi import IOLApi
import asyncio

async def main():
    iol = IOLApi()
    await iol.login(
        username='', # Correo electronico
        password=''
    )
  
    portafolio = await iol.get_portafolio_by_pais(pais='argentina')
    syp500 = [activo for activo in portafolio.activos if activo.titulo.simbolo == 'SPY'][0]
    print(syp500.cantidad)

if __name__ == '__main__':
    asyncio.run(main=main())
```

#### Transformar datos a json

La respuesta de cada método utiliza el decorador "[dataclass](https://docs.python.org/3/library/dataclasses.html)", por lo que, para pasarlo a json hay que hacer

```python
from IOLApi import IOLApi
import asyncio, json
from dataclasses import asdict # <-- Para pasarlo a dict, y luego a json

async def main():
    iol = IOLApi()
    await iol.login(
        username='', # Correo electronico
        password=''
    )
  
    portafolio = await iol.get_portafolio_by_pais(pais='argentina')
    print(json.dumps(asdict(portafolio)))

if __name__ == '__main__':
    asyncio.run(main=main())
```
