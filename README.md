# Проектная работа 9 спринта
link to git -> https://github.com/KseniiaKarpova/ugc_sprint_2

### Описание проекта:
- `TestDataBase` - MongoDB vs Postgres vs Clickhouse. 

```bash
docker-compose -f docker-compose.tests.yaml run auth_api poetry run alembic upgrade head
docker-compose -f docker-compose.main.yaml -f docker-compose.db.yaml -f docker-compose.elk.yaml up --build
```
