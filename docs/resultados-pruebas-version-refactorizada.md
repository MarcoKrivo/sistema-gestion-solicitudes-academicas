# Resultados de pruebas – Versión refactorizada

## Objetivo

Verificar que las funcionalidades del Sistema de Gestión de Solicitudes Académicas continúen funcionando correctamente después del proceso de refactoring.

Se ejecutaron los mismos casos de prueba utilizados en la versión inicial, con el objetivo de comparar los resultados y comprobar que se conserva el comportamiento esperado.

## Casos de prueba

| Código | Caso de prueba | Resultado esperado | Estado |
|---|---|---|---|
| CP01 | Registrar estudiante | El estudiante se registra correctamente. | Aprobado |
| CP02 | Validar campos obligatorios | El sistema rechaza los campos vacíos. | Aprobado |
| CP03 | Correo duplicado | El sistema rechaza un correo ya registrado. | Aprobado |
| CP04 | Registrar responsable | El responsable se registra correctamente. | Aprobado |
| CP05 | Registrar solicitud | La solicitud se registra correctamente. | Aprobado |
| CP06 | Prioridad inválida | El sistema rechaza una prioridad no permitida. | Aprobado |
| CP07 | Cambiar estado | El estado de la solicitud se actualiza correctamente. | Aprobado |
| CP08 | Asignar responsable | El responsable queda asociado a la solicitud. | Aprobado |
| CP09 | Buscar solicitudes | El sistema devuelve los resultados según los filtros. | Aprobado |
| CP10 | Generar reporte | Se muestran los totales y agrupaciones correspondientes. | Aprobado |

**Modalidad:** pruebas funcionales manuales.

## Evidencias

Se adjuntan tres capturas de pantalla como evidencia complementaria de las pruebas realizadas.

Ubicación:

`docs/evidencias/pruebas-version-refactorizada/`

## Conclusión

Los diez casos de prueba ejecutados obtuvieron resultados satisfactorios. Al comparar los resultados con los obtenidos en la versión inicial, se verificó que las funcionalidades principales del sistema continúan operativas después del proceso de refactoring, conservando el comportamiento esperado.

Luego de incorporar las técnicas Extract Method e Introduce Parameter Object y recuperar el filtro por tipo de solicitud, se volvieron a ejecutar los diez casos de prueba funcionales. Los resultados confirmaron que estos cambios no afectaron las funcionalidades existentes.