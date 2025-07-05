# hr_onboarding_LangGraph

I created a multi-agent system for the HR New Employee Joining Process using LangGraph, FastAPI, and a PostgreSQL database.

## Health check

GET http://127.0.0.1:8000/health

## Onboard employee

POST http://127.0.0.1:8000/employee/onboard
Body (JSON):
{
"name": "John Doe",
"email": "john.doe@example.com"
}

## backend run command:

set PYTHONPATH=E:\professional\LangChain\hr_onboarding_LangGraph\backend

uvicorn main:app --reload

## Generate Migration

alembic revision --autogenerate -m "Added new fields to employee table"

## Apply Migration

alembic upgrade head

## alembic Run:

alembic revision --autogenerate -m "Added department field to employee"
alembic upgrade head

## Docker Run:

## If you want your Docker app to use local Postgres (PGAdmin):

docker exec -it hr_onboarding_backend psql -h host.docker.internal -U gopal -d hronboardinglanggraphdb

docker run -it --rm python:3.10-slim bash -c "apt-get update && apt-get install -y iputils-ping && ping host.docker.internal"

docker-compose up --build

## If you want Postgres inside Docker (not local):

docker-compose down -v

docker-compose up --build

E:\softwares\PostgreSQL\17\data\pg_hba.conf
E:\softwares\PostgreSQL\17\data\postgresql.conf
