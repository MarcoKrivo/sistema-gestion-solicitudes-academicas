# Revisión técnica del sistema

## 1. Objetivo

Realizar una revisión técnica de la versión refactorizada del Sistema de Gestión de Solicitudes Académicas, verificando la organización del código, la separación de responsabilidades, la legibilidad y el cumplimiento de buenas prácticas de desarrollo.

## 2. Criterios de revisión

Se utilizó una lista de verificación para evaluar los siguientes aspectos:

- Separación de responsabilidades.
- Organización por capas.
- Claridad en nombres de clases, métodos y variables.
- Evitar duplicación de código.
- Validación de datos de entrada.
- Manejo adecuado de excepciones.
- Separación entre lógica de negocio y acceso a datos.
- Conservación del comportamiento funcional.

## 3. Checklist de revisión aplicado

| Criterio | Resultado | Observación |
|---|---|---|
| Separación de responsabilidades | Cumple | Las responsabilidades están distribuidas entre las distintas capas. |
| Organización por capas | Cumple | Se separaron Router, Services, Repositories, Models y Database. |
| Nombres descriptivos | Cumple | Se utilizan nombres que representan las responsabilidades de clases y métodos. |
| Duplicación de código | Cumple | Se centralizó la conexión a la base de datos. |
| Validación de datos | Cumple parcialmente | Las validaciones principales se encuentran en la capa de servicios. |
| Manejo de excepciones | A mejorar | Se identificó la posibilidad de mejorar la especificidad y consistencia del manejo de errores. |
| Separación de lógica y persistencia | Cumple | Las consultas SQL se encuentran en los repositorios. |
| Conservación del comportamiento | Cumple | Los diez casos de prueba funcionales fueron aprobados. |

## 4. Revisión de la arquitectura

El sistema se organizó en las siguientes capas:

| Capa | Responsabilidad |
|---|---|
| Router | Gestiona la interacción con el usuario mediante el menú. |
| Services | Contiene las reglas de negocio y validaciones. |
| Repositories | Gestiona las operaciones sobre la base de datos. |
| Models | Representa las entidades del sistema. |
| Database | Centraliza la conexión y creación de tablas. |

Esta distribución permite identificar con mayor claridad dónde se encuentra cada responsabilidad y facilita el mantenimiento del sistema.

## 5. Principios y buenas prácticas

Se priorizó el principio de Responsabilidad Única (SRP), distribuyendo las tareas que anteriormente estaban concentradas en el archivo principal.

También se aplicaron criterios de Clean Code mediante nombres descriptivos, separación de responsabilidades y organización del código.

## 6. Observaciones y feedback

Durante la revisión se identificaron los siguientes aspectos:

- La separación por capas mejoró la organización general del proyecto.
- La centralización de la conexión a SQLite evitó repetir esa configuración en distintos módulos.
- Las validaciones de negocio quedaron concentradas en la capa de servicios.
- El manejo de excepciones todavía puede perfeccionarse para ofrecer respuestas más específicas ante distintos errores.

Como aspecto positivo, la nueva estructura facilita la identificación y modificación de responsabilidades sin tener que intervenir directamente en todo el programa.

## 7. Correcciones y criterios de aceptación

Durante el proceso de evolución se realizaron ajustes en la configuración de la conexión a la base de datos y se eliminaron mensajes de depuración que habían sido utilizados durante las pruebas.

Se establecieron los siguientes criterios para considerar aceptada la versión refactorizada:

La aplicación inicia correctamente.

Las tres entidades principales mantienen sus operaciones.

Las funcionalidades originales continúan disponibles.

Los diez casos de prueba funcionales resultan satisfactorios.

La organización por capas permite identificar las responsabilidades de cada módulo.

8. Resultado

La revisión permitió documentar las mejoras estructurales introducidas y reconocer aspectos que pueden continuar perfeccionándose.

Se considera que la versión refactorizada cumple con los criterios funcionales y estructurales evaluados, aunque se identifican oportunidades de mejora en el manejo de excepciones y la validación de entradas.