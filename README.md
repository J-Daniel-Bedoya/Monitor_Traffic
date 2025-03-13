# Sistema de Backups Mikrotik

Sistema web para gestionar backups de dispositivos Mikrotik (.backup y .rsc)

## Características

- Subida de archivos .backup y .rsc de Mikrotik
- Listado de backups guardados
- Descarga de backups
- Eliminación de backups
- Interfaz web intuitiva

## Requisitos

- Python 3.8 o superior
- Flask
- Gunicorn

## Instalación Local

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecutar:
```bash
python app.py
```

## Despliegue en Railway

1. Crear una cuenta en Railway (railway.app)
2. Conectar con el repositorio de GitHub
3. Railway detectará automáticamente la configuración necesaria
4. La aplicación se desplegará automáticamente

## Estructura de Archivos

```
├── app.py              # Aplicación Flask
├── requirements.txt    # Dependencias
├── Procfile           # Configuración para Railway
├── templates/         # Plantillas HTML
│   └── index.html
├── static/           # Archivos estáticos
│   └── js/
│       └── main.js
└── Archivos/         # Carpeta donde se guardan los backups
```

## Notas de Seguridad

- Solo se permiten archivos .backup y .rsc
- Validación de tipos de archivo en todas las operaciones
- Los archivos se almacenan en la carpeta "Archivos/"
