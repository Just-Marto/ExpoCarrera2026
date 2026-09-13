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
- Con un solo comando levantás la web y jugás en `http://localhost:5000` desde la propia notebook
- (No se necesita red ni otros dispositivos — el visitante juega en tu pantalla)

---

## Paso 2 — CTF de 3-4 pasos (Día 2)

Cadena de desafío que el visitante resuelve en ~5 min. Cada paso da la pista del siguiente.

**Prompt para el conjunto:**
> "Creá un mini-CTF web de 4 pasos encadenados, servido como sitio estático o Flask:
> 1. **Pista en el código fuente**: una página normal con una pista escondida en un comentario HTML (se encuentra con F12/ver código fuente).
> 2. **Base64**: la pista es un texto en Base64 que hay que decodificar para obtener una URL o palabra.
> 3. **Archivo oculto**: esa pista lleva a un archivo (ej. /robots.txt o un .txt escondido) con el siguiente dato.
> 4. **Flag final**: una última página donde ingresan la palabra encontrada y ganan.
> Explicame cómo funciona cada paso y dame las soluciones en un archivo `SOLUCIONES.md` aparte (para mí, no para los visitantes)."

**Entregable verificable:**
- Resolvés vos el CTF de punta a punta siguiendo solo las pistas
- Tenés el `SOLUCIONES.md` para ayudar a visitantes trabados

### 2b. Hoja de misión (para imprimir)

**Prompt:**
> "Creá una 'hoja de misión' en HTML imprimible (o markdown) que le dé al visitante el contexto del CTF, las reglas, y un espacio para anotar las pistas que va encontrando. Tono de juego, tipo misión de espía."

**Entregable verificable:**
- Documento listo para imprimir

---

## Paso 3 — Pulido y montaje (Día 3)

### 3a. Cartelería y ranking

**Prompt:**
> "Creá los carteles para la estación: (1) un cartel grande de desafío '¿Podés entrar sin la contraseña?' con la pista del injection en letra chica, (2) instrucciones de acceso (la URL/IP), (3) una plantilla de pizarra de ranking para anotar quién completó el CTF. Formato imprimible."

**Entregable verificable:**
- Carteles listos para imprimir

### 3b. Gancho visual de fondo (opcional, si sobra tiempo)

**Prompt:**
> "Dame un script bash para correr en Kali que ejecute un `nmap` en loop contra el Ubuntu Server (10.0.2.3) mostrando output continuo en pantalla completa, como 'gancho visual' de fondo para la expo. Que se vea llamativo pero sea inofensivo."

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