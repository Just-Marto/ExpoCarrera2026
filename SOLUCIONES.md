# Soluciones del CTF CyberQuest

> **Solo para el presentador.** No mostrar a los visitantes.

## Paso 1 — El código oculto
**Respuesta:** `algoritmo`
**Cómo resolverlo:** Abrir el código fuente de la página con F12 o Ctrl+U. Hay un comentario HTML cerca del inicio que dice `<!-- PISTA: La clave del paso 1 es "algoritmo" -->`.

## Paso 2 — El mensaje cifrado
**Respuesta:** `robots.txt`
**Cómo resolverlo:** El texto `cm9ib3RzLnR4dA==` es Base64. Decodificarlo (en base64decode.org o desde terminal con `echo cm9ib3RzLnR4dA== | base64 -d`) da `robots.txt`.

## Paso 3 — El archivo secreto
**Respuesta:** `cortafuegos`
**Cómo resolverlo:** Navegar a `http://localhost:5000/ctf/robots.txt`. El archivo contiene la línea `CLAVE-PASO-3: cortafuegos`.

## Paso 4 — La flag final
**Respuesta:** `CTF{cortafuegos}`
**Cómo resolverlo:** Combinar la palabra del paso 3 con el formato de flag: `CTF{cortafuegos}`.

## Tips para ayudar visitantes trabados

- **Paso 1:** "¿Probaste hacer click derecho → Ver código fuente?"
- **Paso 2:** "¿Sabés qué es Base64? Buscá un decodificador online"
- **Paso 3:** "El archivo tiene nombre, ¿probaste escribirlo en la barra del navegador?"
- **Paso 4:** "Acordate del formato: CTF{palabra}"
