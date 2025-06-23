# Late Show API

A Flask REST API for managing a Late Night TV show system, built with PostgreSQL, JWT authentication, and MVC architecture.

---

## 🚀 Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. **Install Dependencies**
```bash
pipenv install
pipenv shell
```

### 3. **PostgreSQL Setup**
- Start PostgreSQL:  
  `sudo service postgresql start`
- Create the database and user:
  ```sql
  CREATE USER patience WITH PASSWORD '11189115karanjah';
  CREATE DATABASE late_show_db OWNER patience;
  ```

### 4. **Configure Environment**
Edit `server/config.py`:
```python
SQLALCHEMY_DATABASE_URI = "postgresql://patience:11189115karanjah@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "supersecret"
```

### 5. **Database Migration & Seeding**
```bash
export FLASK_APP=server.app:create_app
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

---

## 🏃‍♂️ How to Run

```bash
export FLASK_APP=server.app:create_app
flask run
```
The API will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🔐 Authentication Flow

- **Register:** `POST /register`  
  `{ "username": "yourname", "password": "yourpassword" }`
- **Login:** `POST /login`  
  `{ "username": "yourname", "password": "yourpassword" }`
- **Protected routes:**  
  Add header: `Authorization: Bearer <your_token>`

---

## 🛣️ API Routes

| Route                      | Method | Auth Required? | Description                        |
|----------------------------|--------|----------------|------------------------------------|
| `/register`                | POST   | ❌             | Register a user                    |
| `/login`                   | POST   | ❌             | Log in and get JWT                 |
| `/episodes`                | GET    | ❌             | List episodes                      |
| `/episodes/<int:id>`       | GET    | ❌             | Get episode + appearances          |
| `/episodes/<int:id>`       | DELETE | ✅             | Delete episode + appearances       |
| `/guests`                  | GET    | ❌             | List guests                        |
| `/appearances`             | POST   | ✅             | Create appearance                  |

---

## 📦 Sample Request/Response

**Register:**
```http
POST /register
Content-Type: application/json

{
  "username": "john",
  "password": "secret"
}
```

**Login:**
```http
POST /login
Content-Type: application/json

{
  "username": "john",
  "password": "secret"
}
```
**Response:**
```json
{
  "access_token": "<JWT_TOKEN>"
}
```

---

## 🧪 Postman Usage

- Import `challenge-4-lateshow.postman_collection.json` into Postman.
- Use the collection to test all endpoints.
- For protected routes, set the `Authorization` header to `Bearer <your_token>`.

---

## 📚 Project Structure

```
server/
├── app.py
├── config.py
├── seed.py
├── models/
│   ├── __init__.py
│   ├── guest.py
│   ├── episode.py
│   ├── appearance.py
│   └── user.py
├── controllers/
│   ├── __init__.py
│   ├── guest_controller.py
│   ├── episode_controller.py
│   ├── appearance_controller.py
│   └── auth_controller.py
```

---

## 🌐 GitHub Repo

[Your GitHub Repo Link Here]

---

## ✅ Submission Checklist

- [x] MVC folder structure
- [x] PostgreSQL used (no SQLite)
- [x] Models + validations complete
- [x] Auth implemented + protected routes
- [x] Seed data works
- [x] All routes work and have been tested in Postman
- [x] Clean, complete README.md
- [x] GitHub repo pushed and shared

---

**Feel free to edit this README to match your project and add more details as you go!**



