# P3 BDD test Verificacion
## Enunciado
Crea una web sencilla usando [Django] o [Flask]

Esta web deberá de tener un formulario muy sencillo con:

-   Un textfield en el que podrás escribir un texto libre (máximo 100 caracteres)
-   Dos botones:
    -   Reset: borra todo lo que haya en el textfield
    -   Execute: Arranca el proceso que habéis hecho de cálculo de palabras▪
-   Un textfield/lista/lo que queráis que muestre las palabras y el número de apariciones de las mismas

El funcionamiento de la web es sencillo:

-   Un usuario (no hace falta login/registro/etc) puede introducir cualquiertexto en el textfield (con un máximo de 100 caracteres)
-   Si el usuario pulsa el botón Reset todo el texto que haya en textfield deberá de desaparecer. En caso de que no hubiera texto escrito el botón Reset no deberá de hacer nada.
-   Si el usuario pulsa el botón Execute y hay texto, la web deberá de mostrar por pantalla un listado con las palabras y el número de apariciones ordenadas de mayor a menor y, de igual forma, deberá de borrarse el texto que aparece en el textfield. En caso de que no hubiera ningún texto el botón no tendrá ningún efecto.
## Software
En esta practica hemos trabajado con Python 3.6, por este motivo, aunque se pedia que la automatización de los test se hiciera con [lettuce], debido a que este software ya no es soportado por Python3, hemos optado por utilizar [aloe]
## Librerias necesarias:
 1. django 
 2. aloe 
 3. aloe-django
 4. nose 
 5. django-nose 
 6. django-nose-selenium 
 7. selenium 
    
## Para que funcione:
- Es necesario el archivo "chromedriver.exe", este archivo se encuentra ya incluido en el proyecto y corresponde a una arquitectura win32, si tu SO no es windows, entra en el [link], descarga la version que se ajuste a tu ordenador e incluye este archivo en la siguiente ruta
		
		 F:\*\P3Verificacion\P3Verificacion\Apps\Web\test_automated\
- Ir a features/browser.py 
- Poner la ruta de chromedriver.exe
			
			e.g. driver = webdriver.Chrome(r'F:\*\P3Verificacion\P3Verificacion\Apps\Web\test_automated\chromedriver.exe')
	
## Ejecución:

- Abrir la terminal e ir hasta el directorio del proyecto y escribir
		
		(venv) F:\*\P3Verificacion> python manage.py runserver

### MANUALMENTE:
 - Abrir el navegador y escribir la ruta
 	 
		localhost:8000/Practica/contador
### AUTOMATIZADO: 
- Abrir otra terminal e ir hasta el directorio test_automated y escribir:

		(venv) F:\*\P3Verificacion\P3Verificacion\Apps\Web\test_automated> aloe
        
## Equipo Desarrollo
1. [Sergio Blanco]
2. [Sergio Cuesta]
3. [Miguel Muñiz]
4. [Miguel Olmedo]

## Version
    V2.0

[Sergio Blanco]: https://github.com/sergioBMPN
[Sergio Cuesta]:https://github.com/scj300
[Miguel Muñiz]: https://github.com/miguelmuniz46
[Miguel Olmedo]: https://github.com/MiguelOlmedo
[Django]:https://www.djangoproject.com
[Flask]:http://flask.pocoo.org/
[link]:https://chromedriver.storage.googleapis.com/index.html?path=2.38/
[lettuce]:http://lettuce.it/
[Aloe]:https://pypi.org/project/aloe/