# Plan de desarrollo — Expo Ing. en Sistemas (Ciberseguridad)

**Objetivo:** Estación interactiva donde el visitante "hackea" un login (SQL injection) + un CTF de 3-4 pasos como gancho, servido desde el Ubuntu Server y accesible por navegador.

**Herramienta:** Claude Code
**Plazo:** < 3 días
**Stack:** Python 3 (Flask o http.server), HTML/CSS/JS plano, SQLite. Sin dependencias pesadas.

**Dónde corre:** Todo en la **notebook de la expo**, en `localhost`. El visitante juega en tu pantalla — NO se necesita red, ni la VM Ubuntu, ni acceso desde otros dispositivos. La VM Ubuntu/Kali queda solo para prácticas de pentesting, no para esta demo.
**Dónde desarrollar:** Directo en la notebook de la expo (mismo entorno donde vas a presentar = cero sorpresas). Si desarrollás en otra máquina, el puente es Git/GitHub (`push` en una, `clone` en la otra).

---

## Cómo trabajar con Claude Code (leer primero)

- Sos el **desarrollador** del desafío, no el que lo resuelve → acá SÍ pedís código completo.
- Pedile que **explique cada pieza** mientras la escribe, sobre todo la parte vulnerable, para que entiendas *por qué* es explotable (esto es lo que vas a explicar en la expo y lo que suma a tu portfolio).
- Trabajá en un repo Git desde el paso 0 → cada etapa es un commit verificable.
- Regla de oro: **verificá cada entregable antes de pasar al siguiente**. No avances si algo no funciona.

---

## Paso 0 — Setup del proyecto (30 min)

**Prompt para Claude Code:**
> "Inicializá un proyecto Python llamado `expo-ciberseguridad`. Creá la estructura de carpetas para dos módulos: `login-vulnerable/` y `ctf/`. Inicializá un repo Git con un .gitignore para Python. Creá un README que explique que es un proyecto educativo para una expo universitaria."

**Entregable verificable:**
- Estructura de carpetas creada
- `git status` funciona, primer commit hecho
- README presente

---

## Paso 1 — Estación "Hackeá el login" (Día 1)

### 1a. Login funcional (base)

**Prompt:**
> "Creá una web con un formulario de login (usuario + contraseña) usando Flask y SQLite. Que tenga una base con 2-3 usuarios de ejemplo. Por ahora que valide correctamente. Diseño limpio tipo 'Campus Virtual Demo' — NO uses marca de ninguna universidad real, algo genérico. Explicame cómo funciona la validación."

**Entregable verificable:**
- La web levanta en `http://localhost:5000`
- Con credenciales correctas entra; con incorrectas, rechaza

### 1b. Introducir la vulnerabilidad (el corazón de la demo)

**Prompt:**
> "Modificá la consulta de login para que sea vulnerable a SQL injection (concatenación directa del input en la query). Comentá el código explicando exactamente por qué es explotable y qué haría un `' OR '1'='1`. Esto es intencional y educativo."

**Entregable verificable:**
- Entrás con `' OR '1'='1` en el campo usuario/contraseña sin conocer credenciales
- Entendés (te lo explicó) por qué funciona

### 1c. Pantalla de "lo lograste" + mensaje educativo

**Prompt:**
> "Cuando el login se bypassa por injection, mostrá una pantalla de éxito que explique en lenguaje simple qué acaba de pasar, por qué fue posible, y cómo se previene (consultas parametrizadas). Agregá un botón 'ver la versión segura' que muestre el mismo login pero corregido, para comparar."

**Entregable verificable:**
- Flujo completo: inject → pantalla ganadora → explicación → versión segura
- La versión segura rechaza el mismo `' OR '1'='1`

### 1d. Correr en localhost + comando de arranque simple

**Prompt:**
> "Dejá la app corriendo en localhost. Creá un script (o instrucción única) para levantar todo con un solo comando, así el día de la expo lo arranco sin pensar. Documentalo en el README."

**Entregable verificable:**
### 1e. A prueba de todo (agregar sobre lo ya hecho en el Paso 1)

Como Claude Code ya está trabajando el login, pasale esto como ajuste, no como algo nuevo:

**Prompt:**
> "Sobre el login que ya estamos armando, agregá dos cosas pensadas para una expo donde
> lo va a usar público general (incluida gente sin conocimientos técnicos):
> 1. Que NINGUNA entrada rara del usuario rompa la app ni muestre un error feo de Python.
>    Si alguien escribe cualquier cosa, la web responde de forma controlada.
> 2. Un botón bien visible de 'volver al inicio' / 'reiniciar', para que después de que
>    una persona juega, la siguiente arranque limpio sin que yo toque nada.
> Explicame qué cambiaste."

**Entregable verificable:**
- Escribís basura en los campos y la web no se cuelga ni muestra error de Python
- Después de ganar, el botón de reinicio deja todo listo para el próximo visitante

---

## Paso 2 — CTF de 3-4 pasos (nivel OPCIONAL "para los que quieren más")

**Concepto de diseño clave:** el CTF NO es para todo el mundo. Se presenta como un
desafío **opcional** para el visitante que ya pasó el login y se copó. El login (Paso 1)
es el "nivel todos" — rápido, garantizado, con la pista servida. El CTF es el "nivel
techo alto" para quien tiene curiosidad técnica. Así nadie se frustra: el despistado
juega el login y se va contento, el capo se queda con el CTF.

Regla de oro del CTF: **piso bajo, ayuda graduada.** Cada paso debe poder resolverse
con la hoja de misión sola, sin que vos tengas que estar al lado. Nadie se traba en el
paso 1 y abandona.

**Prompt para el conjunto:**
> "Creá un mini-CTF web de 4 pasos encadenados, servido con Flask, presentado como
> desafío OPCIONAL (no obligatorio). Cada paso da la pista del siguiente:
> 1. **Pista en el código fuente**: una página con una pista escondida en un comentario HTML (se encuentra con F12 / ver código fuente).
> 2. **Base64**: la pista es un texto en Base64 que hay que decodificar.
> 3. **Archivo oculto**: esa pista lleva a un archivo (ej. /robots.txt o un .txt escondido) con el siguiente dato.
> 4. **Flag final**: una página donde ingresan la palabra encontrada y ganan.
>
> Requisitos importantes de diseño:
> - Cada paso debe tener un sistema de PISTAS GRADUADAS: un botón 'pista' que revela
>   una ayuda cada vez más explícita (pista suave → pista media → casi la respuesta).
>   Así el visitante que se traba se destraba solo, sin frustrarse ni depender de mí.
> - Que ninguna entrada rara del usuario rompa la app (manejo de errores).
> - Dame las soluciones y las pistas graduadas en un archivo `SOLUCIONES.md` aparte (para mí)."

**Entregable verificable:**
- Resolvés vos el CTF de punta a punta siguiendo solo las pistas
- Probás el sistema de pistas graduadas: trabándote a propósito, las pistas te sacan adelante
- Tenés el `SOLUCIONES.md`

### 2b. Hoja de misión (para imprimir)

**Prompt:**
> "Creá una 'hoja de misión' en HTML imprimible que le dé al visitante: el contexto del
> CTF, que es OPCIONAL y para quien quiera un desafío extra, las reglas, cómo pedir
> pistas si se traba, y un espacio para anotar lo que va encontrando. Tono de juego,
> tipo misión de espía. Dejá claro que 'está bien pedir pistas, no es hacer trampa'."

**Entregable verificable:**
- Documento listo para imprimir, con el tono de "desafío opcional sin presión"

---

## Paso 3 — Pulido y montaje (Día 3)

### 3a. Cartelería y ranking

**Prompt:**
> "Creá los carteles para la estación: (1) un cartel grande de desafío '¿Podés entrar sin la contraseña?' con la pista del injection en letra chica, (2) un cartel más chico presentando el CTF como 'desafío OPCIONAL para los que quieren más', (3) una plantilla de pizarra de ranking para anotar quién completó el CTF. Formato imprimible."

**Entregable verificable:**
- Carteles listos para imprimir

### 3b. Gancho visual de fondo (opcional, si sobra tiempo)

Nota: esto usa la VM Kali, es totalmente aparte de la demo web. Solo si te sobra tiempo
y querés algo llamativo de fondo en una segunda pantalla.

**Prompt:**
> "Dame un script bash para correr en Kali que ejecute un `nmap` en loop contra un target de mi laboratorio, mostrando output continuo en pantalla completa, como 'gancho visual' de fondo para la expo. Que se vea llamativo pero sea inofensivo."

**Entregable verificable:**
- El script corre en loop y se ve bien en una pantalla aparte

### 3c. Prueba general

- Prendé el Ubuntu Server, levantá ambos módulos (login + CTF).
- Accedé desde otro dispositivo y jugá el flujo completo como si fueras un visitante.
- Cronometrá: la estación de login debería tomar <2 min, el CTF ~5 min.
- Preparate un guión de 30 segundos para explicarle a quien evalúa: qué es, por qué importa, cómo se previene.

---

## Checklist final (día de la expo)

- [ ] Notebook con Python + Git instalados y probados
- [ ] Ambos servicios (login + CTF) levantan con un solo comando en localhost
- [ ] Probaste el flujo completo en la notebook, como si fueras un visitante
- [ ] Carteles impresos y colocados
- [ ] Hoja de misión impresa (varias copias)
- [ ] Pizarra de ranking + fibrón
- [ ] Credenciales/pistas de demo a la vista
- [ ] Guión de 30s ensayado
- [ ] Preguntas difíciles ensayadas (que Claude Code te tome examen)
- [ ] Notebook cargada / cargador a mano

---

## Notas de seguridad (importante para la expo)

- Todo corre en **localhost**, en tu notebook, nada expuesto a internet ni a la red del evento.
- La web vulnerable es **intencionalmente** insegura y **solo** para la demo — no la dejes corriendo expuesta a una red ni la subas a un hosting público. En GitHub va bien (es código educativo), pero dejá claro en el README que es intencionalmente vulnerable.
- El mensaje central no es "mirá qué fácil es atacar" sino **"mirá cómo se previene"** — eso es lo que valora quien evalúa y lo que te posiciona como alguien que entiende defensa, no solo ataque.

---

## Para tu portfolio (después de la expo)

- Subí el proyecto a GitHub con un buen README (qué demuestra, capturas, cómo correrlo).
- Escribí un write-up estilo lab: qué construiste, la vulnerabilidad, cómo se explota, cómo se mitiga. Encaja perfecto con tu estructura de write-ups bilingüe.
- Este proyecto muestra que sabés **construir** entornos vulnerables, no solo resolverlos — eso pesa.