🚀 Windows Update
Este script es una utilidad para Windows que automatiza la actualización de todos tus programas instalados de una sola vez. 🛠️

🔍 ¿Qué es lo que hace exactamente?
El script utiliza una herramienta oficial de Microsoft llamada Winget (Windows Package Manager). Su función es buscar en internet si existen versiones más nuevas de las aplicaciones que ya tienes instaladas (como Chrome, VLC, Spotify, Zoom, Discord, etc.) y proceder a actualizarlas automáticamente. 📦

🚀 ¿Cómo puedes usarlo?
Tienes dos caminos muy fáciles para poner a funcionar esta herramienta. ¡Ojo! En ambos casos es obligatorio darle "permisos de administrador" para que el script tenga la "llave maestra" y pueda instalar las cosas por ti.

Opción A: Usando el ejecutable (.exe) 🟢
Esta es la opción más rápida, ideal si quieres que todo funcione de inmediato.

¿Cómo se hace?: Busca el archivo que termina en .exe, dale clic derecho con el ratón y elige la opción que dice "Ejecutar como administrador".

Opción B: Copiando el archivo Python (.py) 🐍
Esta opción es ideal si ya tienes Python en tu equipo y quieres ver cómo funcionan las instrucciones por dentro.

¿Cómo se hace?: Necesitas abrir tu ventana de comandos (la terminal) con permisos de administrador y luego escribir el nombre del archivo .py.

💻 ¿Qué sucederá en tu computador al ejecutarlo?
Cuando inicies el script, esto es lo que verás:

🛡️ El Aviso de Windows: Verás una ventana que te pregunta: "¿Quieres permitir que esta aplicación realice cambios en tu dispositivo?". Debes decir que SÍ. Sin este permiso, el script no podrá trabajar.

📟 Apertura de una Ventana Negra (Terminal): Se abrirá una ventana con el título "Windows Update Manager".

🔄 Escaneo del Sistema: El script mirará qué programas tienes y preguntará a Microsoft: "¿Hay algo nuevo?".

📥 Descarga e Instalación: Verás barritas que se llenan. Eso significa que está bajando e instalando las versiones más nuevas.

Nota: No te asustes si ves alguna ventanita aparecer y desaparecer rápido, es el script trabajando.

✅ Finalización: Cuando termine, dirá "Proceso finalizado correctamente" y la ventana se cerrará solita en 5 segundos. ⏳

⚠️ Notas Importantes
Seguridad: Solo se usan herramientas oficiales de Microsoft. Es un proceso muy seguro. 🛡️

Permisos: Si no lo ejecutas como administrador, el script te avisará o simplemente no podrá actualizar nada, porque Windows protege tus programas bajo llave.
