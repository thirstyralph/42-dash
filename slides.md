---
author: QTechGames
date: "2026"
paging: "%d / %d"
---

```text
╔══════════════════════════════════════════════════════════════════════╗
║  SEÑAL INTERCEPTADA — Sector 42, Subred Ω-7                          ║
║  CIFRADO: HMAC-SHA256 (obviamente)                                   ║
║  PRIORIDAD: IMPROBABILIDAD ABSOLUTA                                  ║
║  ESTADO: QUE NO CUNDA EL PÁNICO                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

# La Arena del Agregador

### Un reto de ingeniería de 2–3 horas

> *"En algún lugar del cosmos que funciona con sistemas distribuidos*
> *y café frío, un Operador espera. Tienen 2–3 horas.*
> *Esto, por supuesto, es perfectamente razonable."*

---

# ¿Qué tenéis que construir?

Un **Agregador de Juegos y Portal de Operador** para casino.

El sistema debe:

- 📋 Listar **miles de juegos** de múltiples proveedores
- 🔍 Filtrarlos, ordenarlos y paginarlos
- 🚀 Lanzarlos con sesiones **firmadas criptográficamente**
- 💰 Gestionar una billetera con **transacciones concurrentes**
- 🖥️ Tener una interfaz usable por humanos

El evaluador es automático, frío y determinista.

> *No admira el esfuerzo. Admira los `200 OK`.*

---

# El equipo — Elige tu rol

```text
┌─────────────────────┬────────────────────────┬──────────────────────┐
│  Backend Warden     │  Frontend Illusionist  │  Full-Stack Mage     │
├─────────────────────┼────────────────────────┼──────────────────────┤
│  APIs, validación   │  UI, UX, accesibilidad │  Todo lo anterior    │
│  HMAC, wallet       │  Estado, carga, filtros│  Integración         │
│  95 pts + boss      │  95 pts + boss         │  190 pts (teórico)   │
└─────────────────────┴────────────────────────┴──────────────────────┘
```

Cada arquetipo puede llegar a **~95 puntos perfectos**.

En 2–3 horas, un full-stack realista alcanza **105–115 pts**.

---

# 🛡️ Backend Warden

*"Un 500 no es una respuesta. Es una confesión."*

Responsabilidades:

- Definir contratos API estrictos
- Validar todos los payloads entrantes
- Aplicar reglas de negocio sin excepciones
- Generar tokens de sesión firmados con HMAC-SHA256
- Responder con **códigos HTTP correctos siempre**

```json
// ✅ Así sí
{ "code": "NOT_FOUND", "message": "...", "details": [] }

// ❌ Así no
{ "error": true }   // o peor: HTTP 200 con error dentro
```

---

# 🎨 Frontend Illusionist

*"Si está cargando: spinner. Si está roto: mensaje. Si está en blanco: has fallado."*

Responsabilidades:

- Catálogo de juegos con filtros y paginación
- Vista de detalle con navegación que preserva estado
- Flujo de lanzamiento con estados de carga y error
- Billetera: saldo, apuestas, historial
- **Nunca** página en blanco durante carga

```text
data-testid requeridos:
  game-card  search-input  category-filter  provider-filter
  game-detail  launch-button  mode-selector  loading
  error-message  empty-state  wallet-balance  bet-button
```

---

# ⚡ Full-Stack Battlemage

*"El frontend dice que la API cambió. El backend dice que no. Ambos están equivocados. Yo verifiqué."*

Responsabilidades críticas:

- **Definir el contrato API antes de escribir código**
- Asegurar que frontend y backend hablen el mismo JSON
- Prevenir bloqueos de integración
- Ver el sistema como un organismo único

> Sin este rol, la integración se vuelve... *educativa*.

---

# 📊 El Marcador

```text
┌─────┬────────────────────────────────┬────────┬────────┬───────┐
│  #  │ Prueba                         │ BE pts │ FE pts │ Total │
├─────┼────────────────────────────────┼────────┼────────┼───────┤
│  I  │ El Despertar                   │    5   │    5   │   10  │
│ II  │ El Catálogo del Caos Infinito  │   15   │   15   │   30  │
│ III │ La Inspección del Artefacto    │   10   │   10   │   20  │
│ IV  │ El Ritual de Lanzamiento       │   15   │   15   │   30  │
│  V  │ El Guantelete de Normalización │   15   │    —   │   15  │
│ VI  │ La Bóveda de Txns Infinitas    │   20   │    —   │   20  │
│ VII │ El Sello de Autenticación      │   15   │    —   │   15  │
│VIII │ Estado & UX de Carga           │    —   │   20   │   20  │
│ IX  │ Accesibilidad & Rendimiento    │    —   │   15   │   15  │
│  X  │ El Panel de la Billetera       │    —   │   15   │   15  │
└─────┴────────────────────────────────┴────────┴────────┴───────┘
```

---

# 👾 Los Jefes — Bonus XP

```text
┌──────────────────────────┬────────┬──────────────────────────────┐
│ Jefe                     │ Puntos │ Condición                    │
├──────────────────────────┼────────┼──────────────────────────────┤
│ El Guardián de la Carga  │  +10   │ p95 < 200ms con 50 conc.    │
│ El Centinela Lighthouse  │  +10   │ Performance Lighthouse ≥ 90  │
└──────────────────────────┴────────┴──────────────────────────────┘
```

Son **opcionales** pero posibles con buena implementación.

- **El Guardián**: mutex correcto + respuestas rápidas
- **El Centinela**: gzip, chunk splitting, lazy loading

> No los busquéis al principio. Aparecen solos si hacéis bien el trabajo.

---

# `[NIVEL 0]` Prueba I — El Despertar `[10 pts]`

> *"Primero, demuestra que existes."*

### Backend (5 pts)

```bash
GET /healthz  →  200  {"status": "ok"}
```

### Frontend (5 pts)

- La app carga sin errores de JavaScript
- Hay un `<h1>` o `document.title` no vacío
- Cero excepciones en consola

### 💡 Tip

**Hacedlo primero.** Un health check perfecto vale más que una billetera a medias.
El evaluador falla si no puede contactar con vuestro servidor.

---

# `[NIVEL 1]` Prueba II — El Catálogo `[30 pts]`

### Backend (15 pts) — `GET /api/games`

| Funcionalidad | Parámetros |
|---|---|
| Búsqueda por nombre | `search=` |
| Filtro | `provider=`, `category=`, `enabled=` |
| Ordenación | `sort=name\|rtp`, `order=asc\|desc` |
| Paginación | `page=`, `pageSize=` (default: 1, 20) |

Respuesta debe incluir `meta: { total, page, pageSize, totalPages }`.

### Frontend (15 pts)

Grid con `[data-testid="game-card"]`, buscador con debounce, filtros de categoría y proveedor, paginación o scroll infinito.

---

# `[NIVEL 1]` Prueba III — Inspección del Artefacto `[20 pts]`

### Backend (10 pts) — `GET /api/games/:id`

```json
// ID válido → 200 con objeto completo
// ID inválido → 404 con estructura de error:
{ "code": "NOT_FOUND", "message": "...", "details": [] }
```

### Frontend (10 pts)

- Clic en carta → vista detalle con todos los campos
- Botón atrás preserva filtros y posición de scroll
- URL inexistente → error claro, no página en blanco

### 💡 Tip

El evaluador navega a `/games/id-que-no-existe`.
Si vuestra app explota silenciosamente, perdéis 2 pts.

---

# `[NIVEL 1]` Prueba IV — El Ritual de Lanzamiento `[30 pts]`

### Backend (15 pts) — `POST /api/launch`

```json
// Request
{ "gameId": "game-001", "mode": "real" }

// Response
{
  "sessionId": "sess-abc123",
  "launchUrl": "https://play.example.com/...",
  "expiresAt": "2026-03-16T15:00:00Z"
}
```

⚠️ **Ley sagrada:** juego deshabilitado + modo `real` = **403**.  
Sin excepciones. Sin creatividad. Esta es la ley.

### Frontend (15 pts)

Botón launch, selector demo/real, estado de carga, mensaje de éxito/error, badge visual en juegos deshabilitados.

---

# `[NIVEL 2]` Prueba V — Normalización `[15 pts]`

Tres proveedores con esquemas completamente distintos → una sola API unificada.

```text
Alpha: { "gameId", "title", "returnToPlayer": 95.42, "active": true }
Beta:  { "game_code", "rtp_value": "95.42", "is_enabled": 1 }
Gamma: { "data": { "attributes": { "metrics": { "rtp": 0.9542 } } } }
```

Todos deben aparecer en `GET /api/games` con el mismo esquema.

### 💡 Tips

- Alpha es fácil. Beta tiene tipos raros (RTP como string, fechas DD/MM/YYYY).
- Gamma multiplica RTP × 100 (`0.9542` → `95.42`).
- Haced la normalización primero, antes del wallet. Es la base de todo.

---

# `[NIVEL 2]` Prueba VI — La Bóveda `[20 pts]`

Saldo inicial: **10.000 créditos**. Las Leyes son absolutas:

```text
1. SIN SALDOS NEGATIVOS   — bet falla si fondos insuficientes
2. SETTLE REQUIERE BET    — no se puede liquidar lo que no existe
3. ROLLBACK SOLO UNSETTLED — no se puede revertir lo ya liquidado
4. SETTLED = INMUTABLE    — liquidado es definitivo
5. IDEMPOTENCIA SAGRADA   — mismo transactionId = misma respuesta
```

### ⚠️ El test de estrés

50 goroutines concurrentes disparando apuestas simultáneas.
**El mutex no es opcional.** Sin él, el saldo final será incorrecto.

```go
var mu sync.Mutex
mu.Lock()
defer mu.Unlock()
```

---

# `[NIVEL 2]` Prueba VII — El Sello `[15 pts]`

Las URLs de lanzamiento deben estar **firmadas con HMAC-SHA256**.

```text
Datos a firmar:  gameId|sessionId|expiresAt
Secreto:         variable de entorno LAUNCH_SECRET
```

### `GET /api/verify-launch?token=<sessionId>&sig=<sig>`

```text
✅ Válido + no expirado  →  200
❌ Firma manipulada      →  403  INVALID_SIGNATURE
⏰ Sesión expirada       →  410  SESSION_EXPIRED
❓ Sesión desconocida    →  404  SESSION_NOT_FOUND
```

### 💡 Tip

`crypto/hmac` + `crypto/sha256` + `encoding/hex` en Go.
El evaluador sabe el secreto y va a verificar cada bit.

---

# `[NIVEL 3]` Prueba VIII — Estado & UX `[20 pts]`

La prueba frontend de mayor valor. La diferencia entre producto y demo.

| Criterio | Puntos |
|---|---|
| Loading indicators (no pantalla en blanco) | 4 |
| Error boundary con botón retry | 4 |
| Empty state: "sin resultados" visible | 4 |
| Filtros/búsqueda/página reflejados en URL | 4 |
| Search con debounce (máx 2 requests) | 4 |

### 💡 Tips

- URL params desde el primer momento: `?search=x&category=slots&page=2`
- `useDebounce(value, 300)` — no más de 2 peticiones por búsqueda rápida
- Error boundary a nivel de app, no solo en componentes hoja

---

# `[NIVEL 3]` Prueba IX — Accesibilidad & Performance `[15 pts]`

| Criterio | Puntos |
|---|---|
| Lighthouse accessibility ≥ 80 | 4 |
| Navegación por teclado (Tab) | 3 |
| ARIA + HTML semántico | 3 |
| Lighthouse performance ≥ 70 | 3 |
| Responsive 375px y 1440px | 2 |

### 💡 Tips rápidos

- `<img>` siempre con `alt`. `<input>` siempre con `<label>`.
- Usar `<main>`, `<nav>`, `<section>` — no solo `<div>`.
- `role="status"` en los indicadores de carga.
- gzip en nginx + chunk splitting en Vite = +10 pts de performance.

---

# `[NIVEL 3]` Prueba X — El Panel de la Billetera `[15 pts]`

Interface visual para el sistema de wallet.

| Criterio | Puntos |
|---|---|
| Saldo visible y actualizable | 3 |
| Input de apuesta + botón, saldo decrece | 4 |
| Historial de transacciones (tipo, monto, ID) | 4 |
| Error de fondos insuficientes claro | 2 |
| Responsive a 375px | 2 |

### data-testid requeridos

```text
wallet-balance   bet-amount   bet-button
transaction-list   transaction-item
```

> Si no construiste el backend: conecta tu UI al evaluador de referencia
> en `http://localhost:3000`. Sirve toda la API con CORS activado.

---

# 🗺️ Estrategia — Los primeros 30 minutos

```text
 0–5 min   ▸ Leer README. Elegir roles. No improvisar.
 5–10 min  ▸ Backend y frontend acuerdan el contrato API.
            Esquema de Game. Errores. Antes de codificar.
10–15 min  ▸ Backend: servidor arranca + /healthz.
            Frontend: proyecto creado + datos mock.
15–30 min  ▸ Backend: GET /api/games básico.
            Frontend: catálogo conectado a datos reales.
```

> **La regla de oro:** Haced que algo funcione completamente
> antes de añadir otra cosa.

---

# 💡 Tips Clave

### Backend

- **Validad en la frontera.** No dejéis pasar payloads malformados.
- **mutex en wallet.** Sin él, el test de estrés os destruirá.
- **Errores consistentes siempre:** `{ code, message, details[] }`
- Ejecutad el evaluador localmente antes de hacer push.

### Frontend

- **data-testid desde el principio.** El evaluador los busca.
- **Nunca página en blanco.** Loading → datos o error, siempre.
- **URL como fuente de verdad** para filtros, búsqueda y página.
- Accesibilidad no es un extra: es 7 puntos en Prueba IX.

### Todos

- Comunicad cambios de API inmediatamente.
- `git push` frecuente. El evaluador puntúa el último commit.

---

# 🚀 Cómo Empezar

```bash
# 1. Fork del repositorio
git clone git@github.com:QTechGames/42-dash.git
cd 42-dash

# 2. Levantad el entorno
docker compose up

# 3. Evaluador de referencia en :3000
#    Vuestro backend debe arrancar en :3000
#    Frontend en :5173

# 4. Ejecutad el evaluador cuando queráis
#    (se ejecuta automáticamente en cada PR)
```

### Estructura del repo

```text
42-dash/
├── backend/    ← vuestro backend (reemplazad el binario)
├── frontend/   ← vuestra UI
├── data/       ← datos de juegos (3 proveedores)
└── docker-compose.yml
```

---

```text
 ┌────────────────────────────────────────────┐
 │         T - 180 MINUTOS Y CONTANDO         │
 │                                            │
 │   ██████████████████████░░░░░░░░░░  60%    │
 │                                            │
 │   ESTADO: LISTO PARA COMPILAR              │
 │   CAFÉ: CARGANDO...                        │
 │   MERGE CONFLICTS: INEVITABLES             │
 └────────────────────────────────────────────┘
```

# ¡A por ello!

> Define la API primero. Luego implementa. Luego prueba.
> En ese orden. **Nunca al revés.**

> Y pase lo que pase — cualquier race condition que aparezca,
> cualquier crisis existencial que vuestro `Promise.all` provoque —
>
> **Siempre sabe dónde está tu token de sesión.**

```text
[INFO] Fin de transmisión. La Arena espera.
[WARN] No olvidéis hacer commit.
```
