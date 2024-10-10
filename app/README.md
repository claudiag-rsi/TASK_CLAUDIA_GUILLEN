## Configuración del ambiente

Es recomendable crear un ambiente virtual para manejar las dependencias de manera aislada. Una vez localizado dentro de la carpeta `CAP02_CHALLENGE` Puedes hacerlo ejecutando:

```
python3 -m venv venv
```

Para activar el ambiente virtual, usa el siguiente comando:

En Windows:

```
.\venv\Scripts\activate
```

En Unix o MacOS:

```
source venv/bin/activate
```

## Instalacion de dependencias

Una vez activado el ambiente virtual, instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Ejecutar tu aplicación

Para iniciar tu API FastAPI, ejecuta:

```
uvicorn main:app --reload
```
