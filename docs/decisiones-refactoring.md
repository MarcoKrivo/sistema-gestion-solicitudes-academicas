# Decisiones de diseño y refactoring

## Objetivo

Mejorar la estructura interna del Sistema de Gestión de Solicitudes Académicas mediante la aplicación de principios SOLID y buenas prácticas de Clean Code, conservando las funcionalidades existentes.

## Problemas que se busca resolver

A partir del diagnóstico de la versión inicial, se identificaron los siguientes problemas:

- Concentración de responsabilidades en el archivo principal.
- Mezcla de interacción con el usuario, validaciones y acceso a datos.
- Consultas SQL dentro de funciones de presentación.
- Repetición de operaciones relacionadas con las conexiones a la base de datos.
- Validaciones y valores permitidos distribuidos en distintas funciones.
- Manejo genérico de excepciones.

## Decisiones de diseño

Se propone reorganizar el sistema mediante una arquitectura por capas:

- **Router:** gestionará la interacción con el usuario y el menú de opciones.
- **Service:** contendrá las reglas de negocio y coordinará las operaciones.
- **Repository:** centralizará las consultas y operaciones sobre la base de datos.
- **Model:** representará las entidades principales del sistema.

## Principios y buenas prácticas

Se priorizará la aplicación del principio de responsabilidad única (SRP), buscando que cada componente tenga una función claramente definida.

También se evaluará la aplicación de OCP y DIP cuando corresponda al diseño de los componentes.

Se utilizarán buenas prácticas de Clean Code, como nombres descriptivos, funciones con responsabilidades concretas, menor duplicación y manejo específico de errores.

## Criterio de conservación funcional

Las mejoras se realizarán manteniendo las funcionalidades de la versión inicial: registro de estudiantes, registro de responsables, registro de solicitudes, modificación de estados, asignación de responsables, búsqueda, filtrado y generación de reportes.

Se realizarán pruebas funcionales posteriores para comparar los resultados con los obtenidos en la versión inicial.