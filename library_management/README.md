
## LIBRARY MANAGMENT SYSTEM
 - examples of Hexagonal Architecture (Ports & Adapters)

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
