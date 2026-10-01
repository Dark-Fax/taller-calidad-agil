# Bloque 5: métricas

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)
- Frecuencia de despliegue: 20 despliegues en 28 días (5 por semana, cerca de 0,71 por día)
- Lead time de cambios (mediana, en horas): 20 horas
- Tasa de fallo de cambios: 20 % (4 de 20)
- Tiempo medio de recuperación (horas): 4,5 horas (5, 3, 2 y 8)

Dato extra: 3 de los 4 fallos ocurrieron en despliegues del viernes.

## Cuatro métricas por enfoque
| Enfoque | Métrica | Qué atributo ISO 25010 respalda |
|---|---|---|
| Scrum | Velocidad del sprint (puntos terminados) | Adecuación funcional |
| Scrum | Defectos escapados por sprint | Fiabilidad |
| Scrum | % de historias que cumplen la DoD | Mantenibilidad |
| Scrum | Cumplimiento del objetivo del sprint | Adecuación funcional |
| Kanban | Tiempo de ciclo | Eficiencia de desempeño |
| Kanban | Trabajo en curso (WIP) promedio | Eficiencia de desempeño |
| Kanban | Rendimiento (tareas por semana) | Adecuación funcional |
| Kanban | Tiempo que una tarea espera bloqueada | Mantenibilidad |
| XP | Cobertura de pruebas | Mantenibilidad |
| XP | Pruebas que fallan por semana | Fiabilidad |
| XP | Deuda técnica (malos olores del código) | Mantenibilidad |
| XP | Tiempo de integración continua | Mantenibilidad |
| DevOps | Frecuencia de despliegue | Adecuación funcional |
| DevOps | Lead time de cambios | Adecuación funcional |
| DevOps | Tasa de fallo de cambios | Fiabilidad |
| DevOps | Tiempo medio de recuperación | Fiabilidad |
