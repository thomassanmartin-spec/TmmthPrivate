# EcoTech Solutions

## Como usarlo

1 Instalar las librerias con `pip install -r requirements.txt`
2 Copiar `.env.example` a `.env` y poner la llave de OpenWeatherMap
3 Correr `python main.py`

## Que hace

- Pide entrar con usuario y clave antes de todo
- Muestra el clima de una ciudad y dice si se puede trabajar
- Muestra el valor del dolar euro y UF
- Calcula el pago de un sueldo en otra moneda
- Guarda las consultas en un historial

## Decisiones

- Use requests porque es la libreria oficial mas usada para APIs
- Use mindicador porque da los valores de Chile y no pide llave
- Use OpenWeatherMap para el clima
- La llave va en el archivo env y no queda en el codigo
- Las claves se guardan con bcrypt y nunca en texto plano
- Hay maximo 3 intentos para entrar
- Solo un usuario que entro puede usar el menu
- Los datos se revisan antes de llamar a la API
- Los errores tienen try except y el programa no se cae
- Los mensajes de error no muestran detalles internos
- Se revisan los codigos 200 401 404 429 y 500

## Uso de IA

- Use IA para revisar el codigo y buscar fallas de seguridad
- La IA recomendo poner timeout en las consultas
- La IA recomendo no mostrar el error completo al usuario
- La IA recomendo limitar los intentos para entrar
- Revise cada cambio antes de dejarlo
