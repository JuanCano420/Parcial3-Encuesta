# Sistema de Gestión de Encuestas

## Descripción
Este sistema permite gestionar encuestas, importar grupos de encuestados, generar informes y conectarse con un CRM.

## Estructura
- `app/`: Contiene el código fuente.
- `docs/`: Documentación del proyecto.

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

3. python app/main.py


# Sistema de Gestión de Encuestas

## Descripción
Este proyecto permite la creación, gestión, visualización y respuesta de encuestas. Los administradores pueden crear encuestas, seleccionar preguntas para incluir en ellas, y visualizar las respuestas de los usuarios. Los usuarios pueden responder las encuestas, y sus respuestas se almacenan en un historial accesible para los administradores.

### Funcionalidades principales:
- **Crear Encuestas**: El administrador puede crear una nueva encuesta y seleccionar preguntas predefinidas o personalizadas para incluir en ella.
- **Responder Encuestas**: Los usuarios pueden responder las preguntas de la encuesta, ingresando su nombre, celular y las respuestas a las preguntas.
- **Visualizar Encuestas**: El administrador puede visualizar las encuestas creadas, incluyendo las preguntas asociadas a cada una.
- **Gestionar Preguntas**: El administrador puede agregar, editar y eliminar preguntas predefinidas en el sistema.
- **Historial de Respuestas**: El administrador puede acceder a un historial con todas las respuestas de los usuarios, incluyendo el nombre, celular y las respuestas a las preguntas.

## Requisitos
Este proyecto está desarrollado en Python 3. Las dependencias principales son:
- **Tkinter**: Biblioteca de Python utilizada para crear la interfaz gráfica de usuario. Generalmente viene preinstalada con Python.
- Si se añaden más dependencias en el futuro (como librerías para análisis de datos o integración de APIs), se añadirán a `requirements.txt`.

### Dependencias
Este proyecto actualmente no requiere librerías externas adicionales, solo Python con Tkinter.

## Instalación
1. Clona el repositorio.
   git clone https://github.com/tu-usuario/sistema-gestion-encuestas.git
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

3. python app/main.py