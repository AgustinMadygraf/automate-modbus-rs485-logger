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
pytest
```

---

![CI](https://github.com/<USER>/<REPO>/actions/workflows/ci.yml/badge.svg)

> Para más detalles, revisa el workflow en `.github/workflows/ci.yml` y la configuración en `setup.cfg`.
