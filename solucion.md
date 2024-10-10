El siguiente challenge está diseñado para que aprendas a enfrentarte a un repositorio relativamente grande por primera vez, con la ayuda de un asistente como Cody.

## Explora
1. Crea un nuevo Chat con Cody.
2. 
- `@CAP02_CHALLENGE/app/main.py` Que hace esta app?
```
Basándome en el código proporcionado, esta aplicación FastAPI:

Crea una instancia de FastAPI llamada app

Incluye el router tasks_router importado desde routers, bajo el prefijo "/tasks" y la etiqueta "tasks"

Define una ruta raíz "/" que responde con un mensaje simple "Task Manager API"

Así que en resumen, esta aplicación FastAPI configura un API básico con un router de tareas y una ruta raíz. El router de tareas probablemente maneja diferentes endpoints relacionados a tareas, como crear, leer, actualizar y borrar tareas. Y la ruta raíz simplemente devuelve un mensaje que indica que es una API de administración de tareas.
```
3.1 y 3.2 `@CAP02_CHALLENGE/app/routers/tasks_router.py` para que son los endpoints?
```
Analizando el código del router tasks_router en routers/tasks_router.py, los diferentes endpoints sirven para:

POST / - Crear una nueva tarea

GET /{task_id} - Obtener una tarea por su ID

GET / - Obtener todas las tareas

PUT /{task_id} - Actualizar una tarea existente por su ID

DELETE /{task_id} - Borrar una tarea por su ID

```
3.3 Como esta construida la base de datos?

```
Según el código proporcionado, la base de datos no se define explícitamente en estos archivos.

Lo único relacionado a la base de datos es la importación e invocación de métodos del módulo db en tasks_router.py:

from db import db

# ...

db.add_task(task)

# ...

db.get_task(task_id)

# etc...
```
- 3.4 Como se inicializa el aplicativo?

## Extiende
1. Añade un nuevo endpoint al aplicativo que permita eliminar TODOS los registros de db.
``` Para agregar un nuevo endpoint que elimine todos los registros de la base de datos, se puede hacer lo siguiente:

En el archivo routers/tasks_router.py, importar la función delete_all_tasks desde el módulo db:
from db import delete_all_tasks



Agregar una nueva ruta DELETE en el router:
@tasks_router.delete("/")
async def delete_all_tasks():
    delete_all_tasks()
    return {"message": "All tasks deleted"}



Implementar la función delete_all_tasks() en el módulo db.py:
def delete_all_tasks():
    # Código para limpiar la DB
    pass 



Probar el nuevo endpoint:
DELETE /tasks/



Esto debería invocar el endpoint delete_all_tasks, ejecutar la función en db.py para limpiar la base de datos y devolver un mensaje de confirmación.

Algunos puntos a considerar:

Manejar errores en caso de falla al limpiar la DB
Restringir el endpoint solo a usuarios autorizados
Confirmar la acción antes de borrar todo
Pero básicamente así se puede agregar un endpoint para limpiar la base de datos.
```
2. En el modulo `app/routers/tasks_router.py`, selecciona cada función y desde el módulo de cody, click en Document.


## Corrige

1. `Code Smell Command`

```
Here are 5 potential improvements for the selected Python code:

Add input validation for task_id and task parameters. This would prevent invalid data from being passed to the database methods, improving robustness and security.

Consider using an ORM like SQLAlchemy instead of directly accessing the database. This would allow leveraging features like connection pooling, add an abstraction layer, and make testing easier.

Add logging to trace requests and capture errors/exceptions. This would improve observability and help with debugging issues in production.

Refactor the error handling to use custom exception classes instead of HTTPException. This would allow handling different errors differently and make the code more readable.

Add caching for get_task and get_tasks using something like Redis to improve performance for frequent/repeated requests. The cache can be invalidated on updates/deletes.

Overall, the code generally follows good practices around routing, status codes, response models, etc. The suggestions above are minor improvements that could make the code a bit more robust and production-ready but there are no major issues. The code is reasonably well factored and demonstrates solid Python, FastAPI, and API development skills.

```