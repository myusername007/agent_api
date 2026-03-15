# AGENT API

FastAPI Backend-проект з запитами до агента Claude API з можливими tools
**Стек:** Python 3.12 · FastAPI · Claude API · ChromaDB

## Швидкий старт

```bash
git clone <repo>
cd agent_api

cp .env.example .env

uvicorn main:app --reload
```


## Endpoints

| Назва | Метод | Навіщо |
|------|-----|--------|
| `/upload` | POST | Завантаження документів для пошуку |
| `/agent` |  POST | Виклик агента з можливістю виклику описаних tools|



## Особливості
- agent_api має три інструменти, два з яких симульовані(get_weather, create_ticket)
- Один з інструментів - векторний пошук по документу за допомогою RAG
- Claude API для аналізу і відповіді на питання
- Збереження документів на диск


