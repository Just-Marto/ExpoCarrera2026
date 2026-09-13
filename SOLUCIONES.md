# Soluciones del CTF CyberQuest

> **Solo para el presentador.** No mostrar a los visitantes.

## Paso 1 — El codigo oculto
**Respuesta:** `algoritmo`
**Como resolverlo:** Abrir el codigo fuente de la pagina con F12 o Ctrl+U. Hay un comentario HTML cerca del inicio que dice `<!-- PISTA: La clave del paso 1 es "algoritmo" -->`.

## Paso 2 — El mensaje cifrado
**Respuesta:** `configuracion`
**Como resolverlo:** El texto `Y29uZmlndXJhY2lvbg==` es Base64. Usar el decodificador integrado en la pagina (pegar el texto y hacer click en "Decodificar"). Resultado: `configuracion`.

## Paso 3 — El archivo secreto
**Respuesta:** `cortafuegos`
**Como resolverlo:** Navegar a `http://localhost:5000/ctf/configuracion`. Se muestra un archivo JSON de configuracion interna. El campo `"clave_seguridad"` tiene el valor `cortafuegos`.

## Paso 4 — La flag final
**Respuesta:** `CTF{seguridad_total}`
**Como resolverlo:** Abrir el codigo fuente de la pagina del paso 4 (Ctrl+U). Hay un comentario HTML y una variable JavaScript con la flag: `CTF{seguridad_total}`. Ensena sobre credenciales hardcodeadas.

## Tips para ayudar visitantes trabados

- **Paso 1:** "¿Probaste hacer click derecho → Ver codigo fuente?"
- **Paso 2:** "Copia el texto raro y pegalo en el decodificador que esta en la misma pagina"
- **Paso 3:** "La palabra del paso anterior es el nombre de un archivo... ¿probaste escribirlo en la barra del navegador?"
- **Paso 4:** "¿Te acordas como encontraste la respuesta del paso 1? Esta pagina tambien esconde algo..."
- **Pista 3 = la respuesta:** Si el visitante sigue trabado, la tercera pista de cada paso da la respuesta directa.
