# automate-modbus-rs485-logger

## Integración Continua (CI)

Este proyecto utiliza GitHub Actions para ejecutar automáticamente linters (flake8, black) y tests (pytest) en cada push o pull request a la rama principal.

### Linters
- **flake8**: Verifica el cumplimiento de PEP8 y otros estándares de estilo.
- **black**: Formateador automático de código.

### Tests
- **pytest**: Ejecuta los tests ubicados en la carpeta `tests/`.

### Ejecución local

Instala las dependencias:
```bash
pip install -r requirements.txt
```

Corre los linters:
```bash
flake8 src tests
black --check src tests
```

Corre los tests:

```bash
pytest --cov=src --cov-report=term-missing
```

Esto mostrará un reporte de cobertura de código en la terminal. Puedes ajustar el reporte usando otros formatos de pytest-cov.


---

## Parámetros de reconexión/backoff Modbus

Puedes configurar la resiliencia ante fallos de comunicación Modbus mediante las siguientes variables en tu `.env`:

- `MODBUS_MAX_RETRIES`: Número máximo de reintentos ante error de comunicación (por defecto: 3)
- `MODBUS_BACKOFF_INITIAL`: Tiempo inicial de espera entre reintentos, en segundos (por defecto: 1)
- `MODBUS_BACKOFF_FACTOR`: Factor de backoff exponencial (por defecto: 2)

Ejemplo:

```env
MODBUS_MAX_RETRIES=3
MODBUS_BACKOFF_INITIAL=1
MODBUS_BACKOFF_FACTOR=2
```

Cada vez que falle la lectura de un registro Modbus, el sistema reintentará hasta el máximo configurado, esperando un tiempo creciente entre cada intento.

![CI](https://github.com/<USER>/<REPO>/actions/workflows/ci.yml/badge.svg)

> Para más detalles, revisa el workflow en `.github/workflows/ci.yml` y la configuración en `setup.cfg`.
