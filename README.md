🛡️ SafeVision - Bot-ia2

SafeVision es un bot de Discord de código abierto impulsado por inteligencia artificial y desarrollado en Python. Su objetivo principal es actuar como un sistema automatizado de moderación de contenido en tiempo real, capaz de interceptar, guardar temporalmente y analizar imágenes adjuntas enviadas por los usuarios en cualquier canal del servidor.

🌟 Vista Previa y Demostración

Aquí puedes ver a SafeVision en acción procesando y evaluando imágenes en Discord:

(Si quieres probar el bot en vivo, puedes sumarlo a tu servidor mediante este Enlace de Invitación de SafeVision)

🔬 ¿Cómo Funciona la IA?

SafeVision utiliza un módulo especializado en visión por computadora (model.py) para clasificar imágenes según su contenido:

Recepción del Evento: El bot detecta el comando $check junto con una imagen adjunta enviada en Discord.

Descarga Temporal: Guarda el archivo de manera local (./nombre_imagen.png) para permitir su inspección.

Clasificación por IA: La función get_class(file_path) procesa la imagen a través del modelo de aprendizaje automático previamente entrenado.

Toma de Decisiones:

Inapropiado/Sensible: Si la categoría detectada es "Inapropiado", el bot elimina el mensaje automáticamente del canal y envía una advertencia al usuario citando el porcentaje de confianza alcanzado.

Seguro: Si la imagen es segura, confirma la clasificación y mantiene la conversación fluida.

📸 Capturas de Pantalla

1. Moderación Automatizada (Contenido Inapropiado)

2. Confirmación de Imagen Segura

🚀 Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Mira la sección de Despliegue para conocer cómo desplegar el proyecto en producción.

📋 Pre-requisitos

Qué cosas necesitas para instalar el software y cómo instalarlas:

Python 3.8+ instalado en tu sistema.

Un Bot de Discord creado desde el Discord Developer Portal con los intents de contenido de mensajes (Message Content Intent) activados.

Las dependencias del entorno de Python instaladas.

Para comprobar tu versión de Python instalada:

python --version


🔧 Instalación

Una serie de ejemplos paso a paso que te dicen lo que debes ejecutar para tener un entorno de desarrollo ejecutándose:

Clona el repositorio:

git clone https://github.com/romanvalcar2019-alt/Bot-ia2.git
cd Bot-ia2


Instala las dependencias necesarias:

pip install discord.py typing_extensions


Verifica el módulo de IA:
Asegúrate de que el archivo model.py esté presente en la raíz del proyecto con la función get_class(file_path) implementada y con las librerías del modelo de IA instaladas (por ejemplo, TensorFlow, PyTorch o Scikit-Learn según corresponda).

Configura tu Token de Discord:
Modifica la última línea en main.py con tu token o configúralo mediante variables de entorno (BOT_TOKEN).

Inicia el bot:

python main.py


💡 Ejemplo de Uso (Demo)

Invita a tu bot a un servidor de pruebas en Discord.

Sube una imagen a un canal de texto y añade el comando $check en el comentario del mensaje.

El bot descargará la imagen, ejecutará get_class y responderá:

Si es segura: ✅ Imagen segura. Clasificada como: Normal (95% de certeza).

Si es sensible: ⚠️ Tu imagen fue eliminada por ser clasificada como sensible/inapropiada (98% de certeza) y borrará el mensaje.

⚙️ Ejecutando las Pruebas

Las pruebas de este bot verifican tanto la conexión a la API de Discord como la precisión del modelo de clasificación de imágenes.

🔩 Pruebas End-to-End

Explica qué verifican estas pruebas y por qué:

Verifican que el bot reciba el adjunto, lo almacene localmente en ./, lo pase correctamente por el algoritmo de clasificación y tome la acción adecuada (eliminar o responder).

Ejemplo: Enviar una imagen de prueba mediante el comando $check y verificar en la consola de Python que on_ready() esté activo y la predicción devuelva la tupla (nombre_clase, porcentaje_confianza).

⌨️ Pruebas de Estilo de Codificación

Explica qué verifican estas pruebas y por qué:

Verifican que el código siga las convenciones Estándar de Python (PEP 8) y el manejo asíncrono (async / await) propio de discord.py.

Ejemplo: Ejecutar flake8 o black para asegurar que las sangrías y la estructura de los eventos on_ready y @bot.command() sean correctas.

📦 Despliegue

Para mantener el bot online 24/7 en un servidor de producción:

Puedes alojarlo en servicios como Railway, Render, Heroku o un VPS en la nube (AWS, DigitalOcean).

Seguridad: Recuerda nunca exponer públicamente tu token de Discord en el código subido al repositorio. Utiliza variables de entorno (os.getenv("BOT_TOKEN")).

🛠️ Construido Con

Python 3 - Lenguaje de programación principal.

discord.py - Librería para interactuar con la API de Discord.

Módulo IA (model.py) - Módulo personalizado para la clasificación y evaluación de imágenes.

🖇️ Contribuyendo

Por favor lee el archivo CONTRIBUTING.md para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

📖 Wiki

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra Wiki.

✒️ Autores

Roman Alcar - Trabajo Inicial y Desarrollo - romanvalcar2019-alt






🎁 Expresiones de Gratitud







