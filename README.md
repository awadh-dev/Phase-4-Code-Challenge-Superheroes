#  Superheroes API

A Flask RESTful API for managing heroes, their superpowers, and the strength of their abilities. This project is part of the **Phase 4 Code Challenge** at Moringa School.

---

##  Project Description

This API allows users to:

- View a list of superheroes
- See individual hero details including their powers
- View and update power descriptions
- Create new hero-power connections with strength levels

The API follows RESTful conventions and responds with clean JSON data.

---

##  Features

- `GET /heroes` — Get all heroes
- `GET /heroes/<id>` — Get a hero and their powers
- `GET /powers` — Get all powers
- `GET /powers/<id>` — Get a specific power
- `PATCH /powers/<id>` — Update power description
- `POST /hero_powers` — Create a hero-power connection

---

##  Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite (default database)
- Postman (for API testing)

---

##  Setup Instructions

1. **Clone the repo**
   ```bash
   git clone <your-private-repo-url>
   cd Phase-4-Code-Challenge-Superheroes
