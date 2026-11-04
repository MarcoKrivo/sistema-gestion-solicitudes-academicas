# Decisiones de diseño y refactoring

## 1. Objetivo

Mejorar la estructura interna del Sistema de Gestión de Solicitudes Académicas mediante la aplicación de principios SOLID y buenas prácticas de Clean Code, conservando las funcionalidades existentes.

## 2. Problemas identificados

A partir del diagnóstico de la versión inicial, se identificaron los siguientes problemas:

- Concentración de responsabilidades en el archivo principal.
- Mezcla de interacción con el usuario, validaciones y acceso a datos.
- Consultas SQL dentro de funciones de presentación.
- Repetición de operaciones relacionadas con las conexiones a la base de datos.
- Validaciones y valores permitidos distribuidos en distintas funciones.
- Manejo genérico de excepciones.

## 3. Decisiones de diseño implementadas

Se reorganizó el sistema mediante una arquitectura por capas:

| Componente | Responsabilidad |
|---|---|
| Router | Gestiona la interacción con el usuario y el menú de opciones. |
| Service | Contiene las reglas de negocio, validaciones y coordinación de operaciones. |
| Repository | Centraliza las consultas y operaciones sobre la base de datos. |
| Model | Representa las entidades principales del sistema. |
| Database | Centraliza la conexión y la inicialización de las tablas. |

Esta distribución permitió separar las responsabilidades que anteriormente estaban concentradas en el archivo principal.

## 4. Principios y buenas prácticas aplicados

Se priorizó el principio de Responsabilidad Única (SRP), asignando a cada componente una función específica.

También se aplicaron criterios de Clean Code, como:

- Nombres descriptivos para clases, métodos y variables.
- Separación de responsabilidades.
- Centralización de las operaciones de conexión a la base de datos.
- Concentración de las validaciones de negocio en la capa de servicios.
- Reducción del acoplamiento entre la interacción con el usuario y el acceso a datos.

## 5. Conservación del comportamiento funcional

Durante el proceso de refactoring se mantuvieron las funcionalidades de la versión inicial:

- Registro de estudiantes.
- Registro de responsables.
- Registro de solicitudes.
- Modificación de estados.
- Asignación de responsables.
- Búsqueda y filtrado de solicitudes.
- Generación de reportes.

La conservación del comportamiento se verificó mediante la ejecución de los mismos diez casos de prueba funcionales utilizados en la versión inicial.

## 6. Resultado

La reorganización permitió mejorar la estructura interna del sistema, facilitando la identificación de responsabilidades y el mantenimiento del código, sin modificar las funcionalidades principales.