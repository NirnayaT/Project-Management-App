𝙵𝚘𝚕𝚍𝚎𝚛 𝚂𝚝𝚛𝚞𝚌𝚝𝚞𝚛𝚎

To-do-app/
├── config/
│   ├── database.py
│   ├── enumeration.py
│   └── __init__.py
│
├── models/
│   ├── users.py
│   ├── projects.py
│   ├── tasks.py
│   ├── comments.py
│   └── __init__.py
│
├── schemas/
│   ├── user_payload.py
│   ├── project_payload.py
│   ├── task_payload.py
│   ├── comment_payload.py
│   └── __init__.py
│
├── repository/
│   ├── user_repository.py
│   ├── project_repository.py
│   ├── task_repository.py
│   ├── comment_repository.py
│   ├── repository.py
│   └── __init__.py
│
├── service/
│   ├── user_services.py
│   ├── project_services.py
│   ├── task_services.py
│   ├── comment_services.py
│   └── __init__.py
│
├── router/
│   ├── api.py
│   └── v1/
│       ├── user.py
│       ├── project.py
│       ├── task.py
│       └── __init__.py
├── utils/
│   ├── auth
│       ├── .env
│       ├── jwt_handler.py
│       └── __init__.py
│   ├── sockets
│       ├── handler.py
│       ├── manager.py
│       ├── notification.py
│       └── __init__.py
│   ├── tokens
│       ├── hash.py
│       └── __init__.py
│   └── __init__.py
├── __init__.py
└── main.py
