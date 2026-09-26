SafeVision 🤖

Bot de Discord basado en inteligencia artificial para analizar y clasificar imágenes automáticamente.

📌 Descripción

SafeVision es un bot de Discord desarrollado en Python que utiliza un modelo de inteligencia artificial entrenado para clasificar imágenes.

El usuario puede enviar una imagen al bot mediante el comando $check. El bot descarga temporalmente la imagen y la procesa utilizando un modelo de Keras almacenado en keras_model.h5.

El modelo analiza la imagen y determina a qué categoría pertenece, devolviendo también un porcentaje de confianza para la predicción.

Si la imagen es clasificada como "Inapropiado", el bot elimina el mensaje y avisa al usuario de que la imagen ha sido considerada sensible o inapropiada. Si la imagen pertenece a otra categoría, el bot informa de la clasificación obtenida.

🧠 Funcionamiento del modelo

El archivo model.py se encarga de preparar las imágenes y realizar las predicciones.

El proceso es el siguiente:

Se carga el modelo entrenado desde keras_model.h5.
Se cargan las categorías disponibles desde labels.txt.
La imagen recibida se convierte al formato RGB.
La imagen se adapta a un tamaño de 224 × 224 píxeles.
Los valores de los píxeles se normalizan.
El modelo realiza la predicción.
Se selecciona la categoría con mayor probabilidad.
El resultado se devuelve junto con el nivel de confianza.

Actualmente, el modelo utiliza las categorías indicadas en labels.txt:

Sparrows
Pigeons

El funcionamiento de clasificación está implementado mediante Keras y utiliza Pillow y NumPy para el procesamiento de las imágenes.

💬 Uso del bot

Para analizar una imagen en Discord:

$check

El comando debe utilizarse enviando una imagen como archivo adjunto.

El bot responderá indicando el resultado del análisis y el porcentaje de confianza de la predicción.

📂 Estructura del proyecto
Bot-ia2/
│
├── main.py          # Código principal del bot de Discord
├── model.py         # Procesamiento de imágenes y predicción
├── keras_model.h5   # Modelo de inteligencia artificial entrenado
├── labels.txt       # Categorías utilizadas por el modelo
├── gatos1.jpg       # Imagen de prueba
├── gorrines_1.jpg   # Imagen de prueba
├── gorriones_2.jpg  # Imagen de prueba
└── .gitignore       # Archivos ignorados por Git
⚙️ Tecnologías utilizadas
Python
Discord.py
Keras / TensorFlow
Pillow
NumPy
