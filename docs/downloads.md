# Descargas

## Instalación en Ubuntu/Debian

### Método recomendado (última versión estable):

```bash
# Descargar el paquete .deb más reciente
wget https://github.com/albertomoyano/gbtexpublisher/releases/download/deb-2025.04.19/gbtexpublisher0_0.1.662-0ubuntu1_all.deb

# Instalar con dependencias
sudo apt install ./gbtexpublisher0_0.1.662-0ubuntu1_all.deb
```

### Alternativa manual:
1. Descargar el .deb desde [Releases](https://github.com/albertomoyano/gbtexpublisher/releases)
2. Instalar:
   ```bash
   sudo dpkg -i gbtexpublisher.deb
   sudo apt install -f  # Resuelve dependencias si es necesario
   ```

## Actualización
```bash
# Primero desinstalar la versi贸n anterior
sudo apt remove gbtexpublisher

# Luego instalar la nueva versión como arriba
```

## Descargas por versión

### Versión Actual (v0.1.662)
- **Fecha**: 19 de Abril 2025
- **Descargas**:
  - [gbtexpublisher_0.1.662.deb](https://github.com/albertomoyano/gbtexpublisher/releases/download/deb-2025.04.19/gbtexpublisher0_0.1.662-0ubuntu1_all.deb) (64-bit)
  - [Ver todas las versiones](https://github.com/albertomoyano/gbtexpublisher/releases)

## Soporte Técnico
Si encuentras problemas:
1. Verifica dependencias:
   ```bash
   sudo apt install gambas3-runtime gambas3-gb-qt5
   ```
2. Reporta issues en [GitHub Issues](https://github.com/albertomoyano/gbtexpublisher/issues)

## Historial de Cambios
- **v0.1.662** (19/04/2025):
  - Mejoras en estabilidad
  - Corrección de errores menores

---

[Inicio](index.md) | [Desarrollador](cv.md) | [Descargas](downloads.md)

2025 gbTeXpublisher | [Licencia GPLv3](LICENSE) | Desarrollado con ❤️ en Gambas

