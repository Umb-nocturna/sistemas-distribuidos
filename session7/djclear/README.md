### CAP 1: Install Django

1. Instalar la libreria desde pip
    ```
    pip install Django
    ```

2. Crear el proyecto:
    ```
    django-admin startproject <miproyecto> .  #Linux - mac
    python -m django startproject <miproyecto> .  #win
    ```

3. se crea el proyecto dentro de la carpeta donde me encuentro. 

4. Puedo probar y ver mi nuevo proyecto asi:
    ```
    python manage.py runserver
    ```

5. Me crea el server con le URL para acceder al sitio 

6. Si apaceren pendientes migraciones. Ejecuto el comando:
    ```
    python manage.py migrate
    ```

7. Ya podemos comprobar que no aparecen actualizaciones.

::: warning
*Conclusión: Django instalado en nuestro entorno de desarrollo.*
:::

### CAP 2: Django templating

1. Crear folder "/templates" dentro de proyecto

2. En el "settings.py" se configura rutas para que se usen desde el proyecto asi:

3. Importo la libreria 
    ```
    import os
    ```

4. Configuro la variable global "SETTINGS_PATH" asi:

    ```
    SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
    ```

5. Configuro la ruta del template, asi:    
    ```
    - - TEMPLATES
        "DIRS": [ os.path.join(SETTINGS_PATH, 'templates'),],
    ```
6. Vamos a llamar nuestro primer template.

7. **[[ ENTENDIMIENTO DE TEORIA EL PATRON MVT ]]**

8. inicio por crear la ruta. en "urls.py", agrego:
    ```
    path("inicio/", inicio),
    ```
9. Creo la vista a nivel del proyecto en "views.py", si el archivo no existe se debe crear.

10. Dentro de "views.py" inserto el codigo:
    ```
    from django.shortcuts import render

    def inicio(request):
        """Retorna gestion pagina de inicio"""
        return render(request,"pages/inicio.html",{})
    ```
11. En "urls.py" debo instanciar la clase que renderiza el Template, Como en este caso estamos 
    construyendo el template desde el mismo proyecto, se instancia con el (.), asi:
    ```
    from .views import inicio
    ```
12. Ahora creo mi archivo HTML en la carpeta que especifique. Coloco algo de HTML para ver que es mi pagina.


::: warning
*Conclusión: Se tiene en "templates/pages" las paginas de cada seccion de forma convencional SIN jerarquia de templates.*
:::

#### CAP3: AHORA, JERARQUIA DE TEMPLATES:


1. **[[ ENTENDIMIENTO DE LA JERARQUIA DE TEMPLATES ]]**

2. Creamos los subfolders dentro de la carpeta "/templates" entre ellos "/layouts" y "/includes"

3. Vamos a crear la plantilla del "template", Dentro de "layouts.html" creamos el archivo "base.html"

4. Basicamente dentro de "base.html" vamos a crear 3 espacios dinamicos:
    ```
    {% block title %} {% endblock %}
    ```
    ```
    {% include "includes/header.html" %}
    ```
    ```
    {% block content %}  {% endblock %}
    ```

    ::: warning
    *block, se utiliza para definir áreas reemplazables en una plantilla base que las plantillas hijas pueden sobrescribir. Está relacionado con la herencia de plantillas.
    include, se utiliza para insertar el contenido de una plantilla dentro de otra, permitiendo la reutilización de fragmentos de código quen no cambian.*
    :::

5. Crear dentro de "/templates/includes/" el archivo "header.html".

6. Ahora, se trabaja en la plantilla hija. inicialmente se trabajara desde "/pages/inicio1.html"

7. Primero, se define que esta plantilla depende una plantilla padre, asi:
    ```
    {% extends "layouts/base.html" %}
    ```
8. Luego definimos los "block" con la informacion dinamica, asi
    ```
    {% block title %} << titulo de la pagina >> {% endblock %}
    {% block content %} << contenido de la pagina >> {% endblock %}
    ```



#### CAP4: COMMING SOON

1. TODO




#### Resources.
[Template Free proyecto](https://startbootstrap.com/theme/personal)


