# Tablero Kanban: políticas por columna

Enlace o captura del tablero: ver `docs/tablero.png`

| Columna | Límite WIP | Política de entrada | Política de salida |
|---|---|---|---|
| Por hacer | 8 | Historia priorizada con criterios de aceptación claros | Alguien del equipo la toma y tiene espacio en desarrollo |
| En desarrollo | 3 | Pruebas escritas primero (TDD) | Código listo en un pull request |
| En revisión / pruebas | 2 | Pull request abierto y CI en marcha | Revisión aprobada y CI en verde |
| Listo para desplegar | 3 | Cumple la DoD completa | Se despliega de lunes a jueves, nunca viernes |
| Hecho | Sin límite | Desplegada y verificada en producción | No aplica |
