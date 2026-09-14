# Soluciones del CTF CyberQuest

> **Solo para el presentador.** No mostrar a los visitantes.

## Paso 1 — El codigo oculto
**Respuesta:** `algoritmo`
**Como resolverlo:** Abrir el codigo fuente de la pagina con F12 o Ctrl+U. Hay un comentario HTML cerca del inicio que dice `<!-- PISTA: La clave del paso 1 es "algoritmo" -->`.

## Paso 2 — El mensaje cifrado
**Respuesta:** `configuracion`
**Como resolverlo:** El texto `Y29uZmlndXJhY2lvbg==` es Base64. La pagina tiene un boton "Abrir decodificador Base64" que lleva a `https://www.base64decode.org/es/`; pegar el texto ahi. Resultado: `configuracion`.

## Paso 3 — El archivo secreto
**Respuesta:** `cortafuegos`
**Como resolverlo:** Navegar a `http://localhost:5000/ctf/configuracion`. Se muestra un archivo JSON de configuracion interna. El campo `"clave_seguridad"` tiene el valor `cortafuegos`.

## Paso 4 — El login vulnerable
**Como resolverlo:** No hay respuesta de texto. Desde el paso 4 hay un boton "Ir al login →" que lleva a `/login`. Ahi, usar el boton "Simular ataque de fuerza bruta" (o probar manualmente `admin / admin`). Al entrar exitosamente como admin, el paso 4 se marca como completado automaticamente y se muestra la flag `CTF{seguridad_total}` en la pantalla de victoria.

## Tips para ayudar visitantes trabados

- **Paso 1:** "¿Probaste hacer click derecho → Ver codigo fuente?"
- **Paso 2:** "Buscá 'decodificar base64 online' y pegá el texto raro en el primer resultado"
- **Paso 3:** "La palabra del paso anterior es el nombre de un archivo... ¿probaste escribirlo en la barra del navegador?"
- **Paso 4:** "Anda al login y probá el boton de fuerza bruta — la contraseña de admin es debil"
- **Pista 3 = la respuesta (pasos 1-3):** Si el visitante sigue trabado, la tercera pista da la respuesta directa. En el paso 4, la tercera pista revela la contraseña (`admin`).
