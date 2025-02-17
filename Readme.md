# Readme

## Descripción

Este proyecto contiene un script en Python (`actionVSI.py`) que permite realizar acciones en instancias de Servidor Virtual (VSI) en IBM Cloud utilizando la API de IBM VPC.

## Requisitos

- Python 3.x
- Paquetes de Python: `ibm_vpc`, `ibm_cloud_sdk_core`
- Variables de entorno configuradas:
    - `api_key`: Clave API para autenticación en IBM Cloud.
    - `region`: Región de IBM Cloud donde se encuentran las instancias.
    - `action`: Acción a realizar en las instancias (por ejemplo, `start`, `stop`).
    - `instances_id`: Lista de IDs de las instancias, separadas por comas.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala los paquetes necesarios:
        ```sh
        pip install ibm_vpc ibm_cloud_sdk_core
        ```
3. Configura las variables de entorno necesarias.

## Uso

Ejecuta el script `actionVSI.py` para realizar la acción especificada en las instancias de VSI:
```sh
python actionVSI.py
```

## Notas

- Asegúrate de que las variables de entorno estén correctamente configuradas antes de ejecutar el script.
- Este script desactiva la verificación SSL para la autenticación. Úsalo con precaución.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
