QA AUTOMATION - BYRON CARVAJAL
==============================

Pruebas automatizadas con Python y Pytest:

- E2E del flujo de compra en https://www.saucedemo.com/ con Selenium WebDriver.
- API del modulo User de https://petstore.swagger.io/v2 con requests.


REQUISITOS PREVIOS
------------------
- Python 3.10 o superior
- Google Chrome instalado
- Conexion a internet (la primera ejecucion descarga el chromedriver)


ENTORNO VIRTUAL
---------------
Crear el entorno desde la raiz del proyecto:

    python -m venv venv

Activarlo en Windows:

    venv\Scripts\activate

Activarlo en Linux / macOS:

    source venv/bin/activate


INSTALACION DE DEPENDENCIAS
---------------------------
    pip install -r requirements.txt


EJECUCION DE LA PRUEBA E2E
--------------------------
Desde la raiz del proyecto, con el entorno activado:

    python -m pytest -v tests_e2e/test_saucedemo_e2e.py --html=reports/report_e2e.html --self-contained-html

El reporte queda en reports/report_e2e.html.


EJECUCION DE LA SUITE DE API
----------------------------
Desde la raiz del proyecto, con el entorno activado:

    python -m pytest -v tests_api/test_petstore_users_api.py --html=reports/report_api.html --self-contained-html --log-cli-level=INFO

El reporte queda en reports/report_api.html.

El reporte HTML incluye las trazas de cada peticion y respuesta (entradas,
variables y salidas) en la seccion Captured log call de cada caso. Con
--log-cli-level=INFO las mismas trazas se ven tambien en la consola.

Las pruebas de API comparten un mismo usuario y dependen del orden del
archivo, por lo que hay que ejecutar el archivo completo y no un test suelto.

Los reportes se abren con cualquier navegador y cada ejecucion sobrescribe el
anterior.


ESTRUCTURA DEL PROYECTO
-----------------------
    tests_e2e/test_saucedemo_e2e.py        prueba del flujo de compra completo
    tests_api/test_petstore_users_api.py   ciclo de vida de un usuario en PetStore
    reports/report_e2e.html                reporte de la ultima ejecucion E2E
    reports/report_api.html                reporte de la ultima ejecucion de API
    conftest.py                            fixture "driver" (abre y cierra Chrome)
    requirements.txt                       dependencias con version fijada
    conclusiones.txt                       conclusiones tecnicas del ejercicio
    collections/petstore_user.postman_collection.json
                                           coleccion de Postman con los 5 pasos de API

La coleccion se importa en Postman (Import > File) y se ejecuta en orden.
Usa las variables {{baseUrl}} y {{username}}, definidas en la propia
coleccion; conviene cambiar el username antes de ejecutarla.


QUE VALIDAN LAS PRUEBAS
-----------------------
E2E (SauceDemo):

1. Login con standard_user / secret_sauce.
2. Agrega "Sauce Labs Backpack" y "Sauce Labs Bike Light" al carrito.
3. Comprueba que el carrito tiene exactamente esos dos productos.
4. Completa el checkout con nombre, apellido y codigo postal.
5. Comprueba que el resumen de compra muestra los mismos dos productos.
6. Finaliza la compra y valida el mensaje "THANK YOU FOR YOUR ORDER".

API (PetStore, modulo User):

1. Crear un usuario (POST /user).
2. Buscar el usuario creado (GET /user/{username}).
3. Actualizar el nombre y el correo del usuario (PUT /user/{username}).
4. Buscar el usuario actualizado (GET /user/{username}).
5. Eliminar el usuario (DELETE /user/{username}).

Como comprobacion adicional, se consulta el usuario eliminado y se espera un 404.
