# Resultados de pruebas – Versión refactorizada

## Objetivo

Verificar que las funcionalidades del Sistema de Gestión de Solicitudes Académicas continúen funcionando correctamente después del proceso de refactoring.

Se ejecutaron los mismos casos de prueba utilizados en la versión inicial, con el objetivo de comparar los resultados y comprobar que se conserva el comportamiento esperado.

## Casos de prueba

| Código | Caso de prueba | Resultado esperado | Estado |
|---|---|---|---|
| CP01 | Registrar estudiante | El estudiante se registra correctamente. | Pendiente de completar |
| CP02 | Validar campos obligatorios | El sistema rechaza los campos vacíos. | Pendiente de completar |
| CP03 | Correo duplicado | El sistema rechaza un correo ya registrado. | Pendiente de completar |
| CP04 | Registrar responsable | El responsable se registra correctamente. | Pendiente de completar |
| CP05 | Registrar solicitud | La solicitud se registra correctamente. | Pendiente de completar |
| CP06 | Prioridad inválida | El sistema rechaza una prioridad no permitida. | Pendiente de completar |
| CP07 | Cambiar estado | El estado de la solicitud se actualiza correctamente. | Pendiente de completar |
| CP08 | Asignar responsable | El responsable queda asociado a la solicitud. | Pendiente de completar |
| CP09 | Buscar solicitudes | El sistema devuelve los resultados según los filtros. | Pendiente de completar |
| CP10 | Generar reporte | Se muestran los totales y agrupaciones correspondientes. | Pendiente de completar |

## Evidencias

Las capturas de pantalla correspondientes a las pruebas se encuentran en:

`docs/evidencias/pruebas-version-refactorizada/`

## Conclusión

Los resultados de estas pruebas permiten evaluar si las modificaciones internas realizadas mediante refactoring conservaron el comportamiento funcional de la versión inicial.