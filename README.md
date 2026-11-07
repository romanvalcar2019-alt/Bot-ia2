SafeVision - Bot-ia2

SafeVision es un bot de Discord impulsado por inteligencia artificial diseñado para analizar imágenes adjuntas en los chats, detectar contenido sensible o inapropiado y moderarlo de manera automática en tiempo real.

Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Mira la sección de Despliegue para conocer cómo desplegar el proyecto en producción.

Pre-requisitos 📋

Qué cosas necesitas para instalar el software y cómo instalarlas:

Python 3.8+ instalado en tu sistema.

Un Bot de Discord creado desde el Discord Developer Portal con los intents de contenido de mensajes (Message Content Intent) activados.

Las dependencias del entorno de Python instaladas.

Para comprobar tu versión de Python instalada:

python --version


Instalación 🔧

Una serie de ejemplos paso a paso que te dicen lo que debes ejecutar para tener un entorno de desarrollo ejecutándose:

Clona el repositorio:

git clone https://github.com/romanvalcar2019-alt/Bot-ia2.git
cd Bot-ia2


Instala la librería de Discord para Python:

pip install discord.py typing_extensions


Verifica el módulo de IA:
Asegúrate de que el archivo model.py esté presente en la raíz del proyecto con la función get_class(file_path) implementada.

Configura el Token:
Asegúrate de configurar tu token de bot en main.py o mediante variables de entorno antes de ejecutar.

Inicia el bot:

python main.py


Ejemplo de uso (Demo) 💡

Invita a tu bot a un servidor de pruebas en Discord.

Sube una imagen a un canal de texto y añade el comando $check en el comentario del mensaje.

El bot guardará temporalmente la imagen, la procesará con el modelo de IA (get_class) y responderá:

Si es segura: ✅ Imagen segura. Clasificada como: Normal (95% de certeza).

Si es sensible: ⚠️ Tu imagen fue eliminada por ser clasificada como sensible/inapropiada (98% de certeza) y borrará el mensaje.

Ejecutando las pruebas ⚙️

Las pruebas de este bot verifican tanto la conexión a la API de Discord como la precisión del modelo de clasificación de imágenes.

Analice las pruebas end-to-end 🔩

Explica qué verifican estas pruebas y por qué:

Verifican que el bot reciba el adjunto, lo almacene localmente en ./, lo pase correctamente por el algoritmo de clasificación y tome la acción adecuada (eliminar o responder).

Ejemplo: Enviar una imagen de prueba mediante el comando $check y verificar en la consola de Python que on_ready() esté activo y la predicción devuelva la tupla (nombre_clase, porcentaje_confianza).

Y las pruebas de estilo de codificación ⌨️

Explica qué verifican estas pruebas y por qué:

Verifican que el código siga las convenciones Estándar de Python (PEP 8) y el manejo asíncrono (async / await) propio de discord.py.

Ejemplo: Ejecutar flake8 o black para asegurar que las sangrías y la estructura de los eventos on_ready y @bot.command() sean correctas.

Despliegue 📦

Para mantener el bot online 24/7 en un servidor de producción:

Puedes alojarlo en servicios como Railway, Render, Heroku o un VPS en la nube (AWS, DigitalOcean).

Recuerda nunca expuesto públicamente tu token de Discord en el código subido al repositorio. Utiliza variables de entorno (os.getenv("BOT_TOKEN")).

Construido con 🛠️

Python - Lenguaje de programación principal.

discord.py - Librería para interactuar con la API de Discord.

Módulo IA (model.py) - Módulo personalizado para la clasificación y evaluación de imágenes.

Contribuyendo 🖇️

Por favor lee el CONTRIBUTING.md para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra Wiki.

Versionado 📌

Usamos SemVer para el versionado. Para todas las versiones disponibles, mira los tags en este repositorio.

Autores ✒️

Roman Alcar - Trabajo Inicial y Desarrollo - romanvalcar2019-alt




