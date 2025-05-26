# paolo-novoa-capital-farmer-exam
test
//PARTE 1
// para la solución de este ejemplo utilice la herramienta de inteligencia artificial BLACKBOXAI y le consulte a la inteligencia artificial el mockup del proyecto 

necesito Crear un sistema web básico que genere cotizaciones legales de forma automática que tenga un frontend simple que tenga los siguientes campos: nombre del cliente, correo electronico , tipo de servicio(constitucion de empresa , defensa laboral , consultoria tributaria) , descripcion del caso y un boton de "generar cotizacion"

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Cotizador Legal Automático</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #667eea, #764ba2);
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #333;
    }
    .container {
      background: white;
      padding: 2rem 3rem;
      border-radius: 12px;
      max-width: 480px;
      width: 90%;
      box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    h1 {
      text-align: center;
      color: #4a3fbc;
      margin-bottom: 1rem;
    }
    label {
      display: block;
      margin-top: 1rem;
      font-weight: 600;
      color: #4a3fbc;
    }
    input[type="text"],
    input[type="email"],
    select,
    textarea {
      width: 100%;
      padding: 0.5rem;
      margin-top: 0.25rem;
      border-radius: 6px;
      border: 1.5px solid #ccc;
      font-size: 1rem;
      transition: border-color 0.3s ease;
      resize: vertical;
    }
    input[type="text"]:focus,
    input[type="email"]:focus,
    select:focus,
    textarea:focus {
      border-color: #764ba2;
      outline: none;
    }
    textarea {
      min-height: 80px;
    }
    button {
      margin-top: 1.5rem;
      width: 100%;
      padding: 0.75rem;
      background: #764ba2;
      border: none;
      color: white;
      font-size: 1.1rem;
      font-weight: 700;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
    button:hover {
      background: #5e3680;
    }
    .quote-result {
      margin-top: 2rem;
      padding: 1rem;
      background: #eae6f7;
      border-radius: 8px;
      border-left: 5px solid #764ba2;
      color: #333;
    }
    .quote-result h2 {
      margin-top: 0;
      color: #4a3fbc;
    }
    .quote-item {
      margin-bottom: 0.5rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Cotizador Legal</h1>
    <form id="quoteForm">
      <label for="clienteNombre">Nombre del Cliente</label>
      <input type="text" id="clienteNombre" name="clienteNombre" placeholder="Ej: Juan Pérez" required />

      <label for="clienteEmail">Correo Electrónico</label>
      <input type="email" id="clienteEmail" name="clienteEmail" placeholder="ejemplo@correo.com" required />

      <label for="tipoServicio">Tipo de Servicio</label>
      <select id="tipoServicio" name="tipoServicio" required>
        <option value="" disabled selected>Seleccione un servicio</option>
        <option value="constitucion">Constitución de empresa</option>
        <option value="defensa">Defensa laboral</option>
        <option value="consultoria">Consultoría tributaria</option>
      </select>

      <label for="descripcion">Descripción del Caso</label>
      <textarea id="descripcion" name="descripcion" placeholder="Breve descripción del caso..." required></textarea>

      <button type="submit">Generar Cotización</button>
    </form>

    <div id="resultadoCotizacion" class="quote-result" style="display:none;">
      <h2>Cotización Generada</h2>
      <div class="quote-item" id="resNombre"></div>
      <div class="quote-item" id="resEmail"></div>
      <div class="quote-item" id="resServicio"></div>
      <div class="quote-item" id="resDescripcion"></div>
      <div class="quote-item" id="resPrecio" style="font-weight: 700; color: #764ba2;"></div>
    </div>
  </div>

  <script>
    (function() {
      const form = document.getElementById('quoteForm');
      const resultado = document.getElementById('resultadoCotizacion');
      const resNombre = document.getElementById('resNombre');
      const resEmail = document.getElementById('resEmail');
      const resServicio = document.getElementById('resServicio');
      const resDescripcion = document.getElementById('resDescripcion');
      const resPrecio = document.getElementById('resPrecio');

      // Pricing rules for each service type (in local currency units)
      const precios = {
        constitucion: 1500,
        defensa: 1000,
        consultoria: 1200
      };

      // Service display names
      const nombresServicios = {
        constitucion: "Constitución de empresa",
        defensa: "Defensa laboral",
        consultoria: "Consultoría tributaria"
      };

      form.addEventListener('submit', function(event) {
        event.preventDefault();

        const nombre = form.clienteNombre.value.trim();
        const email = form.clienteEmail.value.trim();
        const servicio = form.tipoServicio.value;
        const descripcion = form.descripcion.value.trim();

        if (!nombre || !email || !servicio || !descripcion) {
          alert("Por favor, completa todos los campos.");
          return;
        }

        // Generate the quote - base price from the service type
        let precioBase = precios[servicio] || 0;

        // Optionally, add a small complexity fee based on description length
        let descripcionLength = descripcion.length;
        let extraCosto = 0;
        if (descripcionLength > 150) {
          extraCosto = 300;
        } else if (descripcionLength > 75) {
          extraCosto = 150;
        }

        let precioFinal = precioBase + extraCosto;

        // Show the quote details
        resNombre.textContent = `Cliente: ${nombre}`;
        resEmail.textContent = `Correo electrónico: ${email}`;
        resServicio.textContent = `Tipo de servicio: ${nombresServicios[servicio]}`;
        resDescripcion.textContent = `Descripción del caso: ${descripcion}`;
        resPrecio.textContent = `Precio estimado: $${precioFinal.toLocaleString()} COP`;

        resultado.style.display = 'block';
      });
    })();
  </script>
</body>
</html>

// luego procedí a unir los 3 puntos solicitados por el cliente

AHORA DEBO INCLUIR un endpoint que reciba datos del formulario y devuelva una cotizacion en formato json se debe incluir: Numero de cotizacion unico(formato: COT-2025-XXXX), precio segun tipo de servicio(CONSTITUCION DE EMPRESA:1500 SOLES , DEFENSA LABORAL:2000 SOLES Y CONSULTORIA TRIBUTARIA: 800 SOLES) , fecha de creacion y datos ingresados por el cliente.
ademas necesito incluir una base de datos SQLITE con los siguiente campos: ID, NUMRO DE COTIZACION, NOMBRE DEL CLIENTE , EMAIL , TIPO DE SERVICIO, PRECIO Y FECHA.
Y NECESITO INSTRUCCIONES BREVES PARA EJECUTAR EL PROYECTO TODO TIENE QUE ESTAR UNIDO

Estructura del Proyecto

    Archivo HTML: cotizador-legal.html
    Archivo del Servidor: server.py
    Base de Datos: cotizaciones.db

1. Archivo HTML (cotizador-legal.html)

Modificaremos el archivo HTML para enviar los datos del formulario al servidor.

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Cotizador Legal Automático</title>
  <style>
    /* Estilos omitidos por brevedad */
  </style>
</head>
<body>
  <div class="container">
    <h1>Cotizador Legal</h1>
    <form id="quoteForm">
      <label for="clienteNombre">Nombre del Cliente</label>
      <input type="text" id="clienteNombre" name="clienteNombre" placeholder="Ej: Juan Pérez" required />

      <label for="clienteEmail">Correo Electrónico</label>
      <input type="email" id="clienteEmail" name="clienteEmail" placeholder="ejemplo@correo.com" required />

      <label for="tipoServicio">Tipo de Servicio</label>
      <select id="tipoServicio" name="tipoServicio" required>
        <option value="" disabled selected>Seleccione un servicio</option>
        <option value="constitucion">Constitución de empresa</option>
        <option value="defensa">Defensa laboral</option>
        <option value="consultoria">Consultoría tributaria</option>
      </select>

      <label for="descripcion">Descripción del Caso</label>
      <textarea id="descripcion" name="descripcion" placeholder="Breve descripción del caso..." required></textarea>

      <button type="submit">Generar Cotización</button>
    </form>

    <div id="resultadoCotizacion" class="quote-result" style="display:none;">
      <h2>Cotización Generada</h2>
      <div class="quote-item" id="resCotizacion"></div>
      <div class="quote-item" id="resPrecio"></div>
      <div class="quote-item" id="resFecha"></div>
    </div>
  </div>

  <script>
    (function() {
      const form = document.getElementById('quoteForm');
      const resultado = document.getElementById('resultadoCotizacion');
      const resCotizacion = document.getElementById('resCotizacion');
      const resPrecio = document.getElementById('resPrecio');
      const resFecha = document.getElementById('resFecha');

      const precios = {
        constitucion: 1500,
        defensa: 2000,
        consultoria: 800
      };

      form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const nombre = form.clienteNombre.value.trim();
        const email = form.clienteEmail.value.trim();
        const servicio = form.tipoServicio.value;
        const descripcion = form.descripcion.value.trim();

        if (!nombre || !email || !servicio || !descripcion) {
          alert("Por favor, completa todos los campos.");
          return;
        }

        const response = await fetch('/api/generar_cotizacion', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            nombre,
            email,
            servicio,
            descripcion
          })
        });

        const data = await response.json();

        if (response.ok) {
          resCotizacion.textContent = `Número de Cotización: ${data.numero_cotizacion}`;
          resPrecio.textContent = `Precio estimado: ${data.precio} SOLES`;
          resFecha.textContent = `Fecha de creación: ${data.fecha_creacion}`;
          resultado.style.display = 'block';
        } else {
          alert(data.error);
        }
      });
    })();
  </script>
</body>
</html>

2. Archivo del Servidor (server.py)

Este archivo manejará las solicitudes y la base de datos SQLite.

from flask import Flask, request, jsonify
import sqlite3
import datetime
import random

app = Flask(__name__)

# Conexión a la base de datos SQLite
def init_db():
    conn = sqlite3.connect('cotizaciones.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cotizaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_cotizacion TEXT UNIQUE,
            nombre_cliente TEXT,
            email TEXT,
            tipo_servicio TEXT,
            precio REAL,
            fecha TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Generar un número de cotización único
def generar_numero_cotizacion():
    return f"COT-2025-{random.randint(1000, 9999)}"

@app.route('/api/generar_cotizacion', methods=['POST'])
def generar_cotizacion():
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    servicio = data.get('servicio')
    descripcion = data.get('descripcion')

    precios = {
        'constitucion': 1500,
        'defensa': 2000,
        'consultoria': 800
    }

    precio = precios.get(servicio)
    if precio is None:
        return jsonify({'error': 'Tipo de servicio no válido.'}), 400

    numero_cotizacion = generar_numero_cotizacion()
    fecha_creacion = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Guardar en la base de datos
    conn = sqlite3.connect('cotizaciones.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cotizaciones (numero_cotizacion, nombre_cliente, email, tipo_servicio, precio, fecha)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (numero_cotizacion, nombre, email, servicio, precio, fecha_creacion))
    conn.commit()
    conn.close()

    return jsonify({
        'numero_cotizacion': numero_cotizacion,
        'precio': precio,
        'fecha_creacion': fecha_creacion
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

3. Base de Datos (cotizaciones.db)

La base de datos se creará automáticamente al ejecutar el servidor por primera vez, gracias a la función init_db() en server.py.

// Instrucciones para Ejecutar el Proyecto

    1- Instalar Dependencias: Asegúrate de tener Python y pip instalados. Luego, instala Flask ejecutando:

    pip install Flask


2- Crear el Archivo HTML: Crea un archivo llamado cotizador-legal.html y copia el contenido del primer bloque de código.

3-Crear el Archivo del Servidor: Crea un archivo llamado server.py y copia el contenido del segundo bloque de código.

4- Ejecutar el Servidor: En la terminal, navega al directorio donde se encuentran los archivos y ejecuta:

python server.py


5- Abrir el Frontend: Abre el archivo cotizador-legal.html en tu navegador. Asegúrate de que el servidor esté en ejecución.

6- Probar la Aplicación: Completa el formulario y haz clic en "Generar Cotización". Deberías ver la cotización generada en la página.

// PARTE 2

// utilizando la herramienta de inteligencia artificial de blackbox solicite la parte 2 de nuestro test : necesito integrar una inteligencia artificial para enriquecer la cotizacion legal con inteligencia artificial los requerimientos son: analisis de complejidad( nivel de complejidad(baja,media o alta), recomendacion de ajuste de precio(0% , 25% o 50%) y servicios adicionales sugeridos(si corresponde) ademas tiene que generar una automatizacion de propuesta usando IA que genere texto profesional que incluya: servicios incluidos, tiempo estimado y condiciones basicas(tiene que tener como 2 o 3 parrafos profesionales , como si fuera una propuesta enviada a un cliente)

BLACKBOXAI

Para integrar una inteligencia artificial que enriquezca la cotización legal, puedes seguir un enfoque estructurado que aborde cada uno de los requerimientos que mencionas. Aquí te presento un esquema general que podrías considerar:
1. Análisis de Complejidad

    Nivel de Complejidad: Desarrolla un modelo de IA que evalúe la complejidad del caso basado en ciertos parámetros, como la cantidad de documentos, la naturaleza del caso, y la experiencia previa en casos similares. Puedes clasificar la complejidad en tres niveles:
        Baja: Casos simples, pocos documentos, bajo riesgo.
        Media: Casos moderados, varios documentos, riesgo moderado.
        Alta: Casos complejos, muchos documentos, alto riesgo.

2. Recomendación de Ajuste de Precio

    Basado en el análisis de complejidad, el sistema puede sugerir un ajuste de precio en función de la complejidad detectada:
        0%: Para casos de baja complejidad.
        25%: Para casos de complejidad media.
        50%: Para casos de alta complejidad.

3. Servicios Adicionales Sugeridos

    La IA puede analizar el caso y sugerir servicios adicionales que podrían ser relevantes, como:
        Consultas adicionales.
        Servicios de mediación.
        Asesoría legal especializada.

4. Generación de Propuestas Automatizadas

    Utiliza un modelo de procesamiento de lenguaje natural (NLP) para generar texto profesional. La propuesta podría incluir:
        Servicios Incluidos: Detallar los servicios que se ofrecerán.
        Tiempo Estimado: Proporcionar un cronograma aproximado para la finalización del trabajo.
        Condiciones Básicas: Incluir términos y condiciones generales.

Ejemplo de Texto de Propuesta

Aquí tienes un ejemplo de cómo podría estructurarse el texto de la propuesta:

Propuesta de Servicios Legales

Estimado [Nombre del Cliente]:

Nos complace presentarle nuestra propuesta para la gestión de su caso relacionado con [descripción breve del caso]. Tras un análisis exhaustivo, hemos determinado que la complejidad de este asunto es de nivel [bajo/medio/alto], lo que nos permite ofrecerle un enfoque adaptado a sus necesidades específicas.

Los servicios incluidos en esta propuesta abarcan [detallar servicios], con un tiempo estimado de [indicar tiempo] para la finalización. Además, consideramos que podrían ser beneficiosos los siguientes servicios adicionales: [listar servicios adicionales, si corresponde].

Las condiciones básicas de nuestra colaboración son las siguientes: [detallar condiciones]. Estamos comprometidos a brindarle un servicio de alta calidad y a mantenerlo informado en cada etapa del proceso.

Agradecemos la oportunidad de trabajar con usted y quedamos a su disposición para cualquier consulta adicional.

Atentamente,

[Tu Nombre]
[Tu Cargo]
[Nombre de la Firma]
[Datos de Contacto]
Implementación

Para implementar esta solución, necesitarás:

    Un equipo de desarrollo que pueda crear y entrenar los modelos de IA.
    Acceso a datos históricos para entrenar el modelo de análisis de complejidad.
    Herramientas de procesamiento de lenguaje natural para la generación de texto.

Este enfoque te permitirá enriquecer tus cotizaciones legales y ofrecer un servicio más personalizado y eficiente a tus clientes.

Utilizando el ejemplo brindado:

Aquí tienes un ejemplo de código que implementa la función analizar_con_ia, que utiliza un modelo de IA para analizar un caso legal y generar una propuesta profesional. Este código incluye una llamada a una API de IA (como OpenAI) y devuelve un diccionario con los resultados del análisis.


import openai  # Asegúrate de tener la biblioteca OpenAI instalada

# Configura tu cliente de OpenAI
openai.api_key = 'tu_api_key_aqui'

def analizar_con_ia(descripcion, tipo_servicio):
    prompt = f"""
    Analiza este caso legal: {descripcion}
    Tipo de servicio: {tipo_servicio}
    
    Evalúa:
    1. Complejidad (Baja/Media/Alta)
    2. Ajuste de precio recomendado (0%, 25%, 50%)
    3. Servicios adicionales necesarios
    4. Genera propuesta profesional para cliente
    """
    
    # Llamada a la API de IA
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # O el modelo que estés utilizando
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Procesar la respuesta
    respuesta_texto = response['choices'][0]['message']['content']
    
    # Aquí puedes implementar lógica para extraer la información necesaria de respuesta_texto
    # Por simplicidad, se devuelve un ejemplo estático
    return {
        'complejidad': 'Media',  # Extraer de respuesta_texto
        'ajuste_precio': 25,     # Extraer de respuesta_texto
        'servicios_adicionales': ['Revisión de contratos'],  # Extraer de respuesta_texto
        'propuesta_texto': respuesta_texto  # Texto generado por IA
    }

# Ejemplo de uso
resultado = analizar_con_ia("Caso de incumplimiento de contrato", "Asesoría legal")
print(resultado)



  1- API Key: Asegúrate de reemplazar 'tu_api_key_aqui' con tu clave de API de OpenAI.
  2- Modelo: Puedes cambiar el modelo a uno que se ajuste mejor a tus necesidades.
  3- Procesamiento de Respuesta: En el ejemplo, se devuelve un resultado estático. Deberías implementar lógica para extraer la complejidad, ajuste de precio y servicios adicionales de respuesta_texto según el formato que devuelva la IA.
  4- Manejo de Errores: Considera agregar manejo de errores para la llamada a la API, en caso de que falle o devuelva un error.

