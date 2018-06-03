# P4 Final Verificacion
## Enunciado
Partiendo de [la practica anterior] se pide desarrollar:
-  Herramienta web que conste de una forma de, introducida una url de una fuente de información (periódico, revista, blog…), acceda al texto del artículo y muestre de manera ordenada las palabras utilizadas.
-  Estos datos se guardarán en alguna base de datos y permitirá la consulta del número de palabras más utilizadas por día

Esta web deberá de tener un formulario muy sencillo con:

-   Un textfield en el que podrás escribir una URL
-   Dos botones:
    -   Reset: borra todo lo que haya en el textfield
    -   Execute: Arranca el proceso que habéis hecho de cálculo de palabras
    
El funcionamiento de la web es sencillo:
-   Si el usuario pulsa el botón Reset todo el texto que haya en textfield deberá de desaparecer. En caso de que no hubiera texto escrito el botón Reset no deberá de hacer nada.
-   Si el usuario pulsa el botón Execute y hay texto, la web deberá de mostrar por pantalla un listado con las palabras y el número de apariciones ordenadas de mayor a menor y, de igual forma, deberá de borrarse el texto que aparece en el textfield. En caso de que no hubiera ningún texto el botón no tendrá ningún efecto.

## Software
Hemos utilizado las mismas [librerias] para python, además hemos implementado una base de datos en [Redis] para almacenar las palabras mas repetidas, por ultimo, utilizamos [Jenkins] para la integración continua y [ngrok] para levantar el servicio de jenkins.
    
## Para que funcione
Para el desarrollo de esta practica hemos lanzado un servidor de ubuntu, en el que hemos instalado Jenkins. Hemos querido enlazar el servicio de Jenkins con nuestro repositorio de Github, con el fin de que se ejecuten los test cada vez que se envie un nuevo push. Para ello hemos tenido que añadir un [plugin] a Jenkins y lanzar un servicio online con la herramienta gnrok, que abre la aplicacion de Jenkins a Github.
Una vez hecho esto, hemos configurado el repositorio de Github, en el apartado settings->webhooks, seleccionamos la URL del payload generada por gnrok seguido de /github-webhook/

      e.g. http://b3099296.ngrok.io/github-webhook/

## Equipo de desarrollo
1. [Sergio Blanco]
2. [Sergio Cuesta]
3. [Miguel Muñiz]
4. [Miguel Olmedo]

## Version
    V1.4
[Sergio Blanco]: https://github.com/sergioBMPN
[Sergio Cuesta]:https://github.com/scj300
[Miguel Muñiz]: https://github.com/miguelmuniz46
[Miguel Olmedo]: https://github.com/MiguelOlmedo
[la practica anterior]:https://github.com/sergioBMPN/Practica3_BDD_Verificacion/
[Jenkins]:https://jenkins.io/
[Redis]:https://redis.io/
[librerias]:https://github.com/sergioBMPN/Practica3_BDD_Verificacion/blob/master/README.md#software
[ngrok]: https://ngrok.com/
[plugin]:https://wiki.jenkins.io/display/JENKINS/GitHub+Plugin#GitHubPlugin-GithubPlugin

