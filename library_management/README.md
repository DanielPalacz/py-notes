
## LIBRARY MANAGMENT SYSTEM
 - example of Hexagonal Architecture (Ports & Adapters)

```
Hexagonal Architecture:
 - allow to create system that are testable and extendable
 - business logic (app core) separation from: external technologies and services, user interfaces

Key concepts:
 - layers and boundaries:
    - core
    - ports (interfaces)
    - adapters
 - hexagon structure view
 - technology independance 
 
```


## Project structure:
```
library_management/
├── core/
│   ├── __init__.py
│   ├── models.py       # Business logic
│   ├── ports.py        # Interfaces (Ports)
│   └── services.py     # Business services
├── infrastructure/
│   ├── __init__.py
│   ├── db_adapter.py   # Database Adapter
│   └── api_adapter.py  # API Adapter
├── app.py              # Entry point to the app
└── requirements.txt
```
