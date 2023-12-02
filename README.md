# guitar-page

## Descripción

Este proyecto es un e-commerce dedicado a la venta de guitarras. Utiliza Django para gestionar la base de datos y presenta un front-end desarrollado con HTML, CSS, JavaScript y Bootstrap.

## Características

- **Registro de Usuarios:** Los usuarios pueden registrarse, iniciar sesión y gestionar sus cuentas.

- **Catálogo de Guitarras:** Muestra una variedad de guitarras disponibles para la compra.

- **Carrito de Compras:** Permite a los usuarios añadir guitarras al carrito y proceder al pago.

- **Proceso de Pago:** Integración de un proceso de pago seguro para completar las transacciones.

- **Administración:** Un panel de administración de Django para gestionar productos, pedidos y usuarios.

## Tecnologías Utilizadas

- **Django:** Marco de desarrollo web de alto nivel en Python. Facilita la gestión de la base de datos mediante modelos y proporciona una sólida lógica de backend.

- **HTML, CSS, JS:** Tecnologías estándar para el desarrollo del front-end.

- **Bootstrap:** Biblioteca de diseño para una interfaz de usuario rápida y moderna.

## Configuración del Proyecto

**Clonar el repositorio:**
  ```bash
  git clone https://github.com/TomiAltero/guitar-page.git
  ```

### Requisitos previos
<hr>

**python 3.10 requerido:**

*input:*
```bash
python3 --version 
```

*output:*
```bash
Python <numeroVersion>
```

<hr>

**Django requerido:**

*input:*
```bash
    pip install Django
```
<hr>


**Pipenv requerido (o cualquier gestor de entornos virtuales. En este caso utilizamos pipenv):**

*input:*
```bash
    pip install pipenv
```

<hr>

**Debe crear un archivo que se llame *local_settings.py* en config**
```python
from .settings import *
from .settings import DATABASES


DATABASES['default']['PASSWORD'] = 'Ingrese su contraseña'


#opcional, esta en el settings.py
SECRET_KEY = 'Ingrese su secret_key' 

#esta en el settings.py
DEBUG = True

#esta en el settings.py
STATIC_URL = 'static/'

```

En el desarrollo de aplicaciones con Django, es común usar un archivo llamado local_settings.py. Este archivo se utiliza para manejar configuraciones específicas del entorno local o de desarrollo.En lugar de modificar directamente esas configuraciones globales cada vez que trabajas en tu computadora, puedes usar local_settings.py como una especie de "ajuste personal". Este archivo actúa como una extensión de las configuraciones principales y te permite hacer ajustes locales sin afectar la configuración que comparten todos los desarrolladores.