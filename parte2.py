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
