QA AUTOMATION - BYRON CARVAJAL
==============================

Prueba E2E del flujo de compra en https://www.saucedemo.com/ con Python,
Pytest y Selenium WebDriver.


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

    python -m pytest -v --html=reports/report_e2e.html --self-contained-html

El reporte queda en reports/report_e2e.html y se abre con cualquier navegador.
Cada ejecucion sobrescribe el reporte anterior.


ESTRUCTURA DEL PROYECTO
-----------------------
    tests_e2e/test_saucedemo_e2e.py   prueba del flujo de compra completo
    tests_api/                        reservado para las pruebas de API
    reports/report_e2e.html           reporte de la ultima ejecucion
    conftest.py                       fixture "driver" (abre y cierra Chrome)
    requirements.txt                  dependencias con version fijada
    conclusiones.txt                  conclusiones tecnicas del ejercicio


QUE VALIDA LA PRUEBA
--------------------
1. Login con standard_user / secret_sauce.
2. Agrega "Sauce Labs Backpack" y "Sauce Labs Bike Light" al carrito.
3. Comprueba que el carrito tiene exactamente esos dos productos.
4. Completa el checkout con nombre, apellido y codigo postal.
5. Comprueba que el resumen de compra muestra los mismos dos productos.
6. Finaliza la compra y valida el mensaje "THANK YOU FOR YOUR ORDER".
