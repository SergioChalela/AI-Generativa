# Proyecto Asistente Virtual con IA Generativa

Este es un proyecto de **asistencia virtual** utilizando **FastAPI** y **OpenAI GPT**. Está diseñado para simular una conversación en el contexto de un **servicio de atención al cliente** para una empresa ficticia llamada **Sergio Tech**.

## Descripción

Sergio Tech es una empresa que ofrece servicios de **machine learning**, **análisis de datos** y **consultoría de mercado** a **startups**. Este proyecto utiliza un modelo generativo de IA (OpenAI GPT) para proporcionar respuestas automáticas a los clientes sobre los servicios que ofrece la empresa.

El sistema permite:
- Interacción con el modelo de lenguaje GPT para responder preguntas.
- Personalización de las respuestas utilizando un historial de conversación.
- Despliegue en contenedores Docker y en la nube a través de AWS.

## Tecnologías utilizadas

- **FastAPI**: Framework para construir APIs rápidas y eficientes.
- **OpenAI GPT**: Modelo de lenguaje generativo de OpenAI.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **Docker**: Para la contenedorización de la aplicación.
- **AWS**: Para el despliegue en la nube (opcional).
- **Python 3.9**: Lenguaje de programación.

## Requisitos previos

1. **Python 3.9 o superior**
2. **Docker**: Para crear contenedores y desplegar la aplicación.
3. **AWS (opcional)**: Si deseas desplegar la aplicación en la nube.

## Instalación

### Paso 1: Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>
