# Josh_Assignment
# Shantanu Raut

## Features
- **Create Tasks** with a name & description
- **Assign Tasks** to users
- **Fetch Tasks** assigned to a specific user

## Setup Instructions

### Prerequisites
Ensure you have **Python 3.8+** installed.

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:s4shantanu/Josh_Assignment.git
cd task-management-api
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the Database
Run migrations to set up the database.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (For Admin Access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Your API will be available at `http://127.0.0.1:8000/api/`

---

## API Endpoints

### **Create a Task**
- **URL:** `POST /api/tasks/create/`
- **Request Body:**
```json
{
    "name": "Fix API Bug",
    "description": "Fix the 404 error when accessing /api."
}
```
- **Response (`201 Created`):**
```json
{
    "id": 1,
    "name": "Fix API Bug",
    "description": "Fix the 404 error when accessing /api.",
    "created_at": "2025-03-25T12:00:00Z",
    "status": "Pending"
}
```

### **Get Tasks for a User**
- **URL:** `GET /api/tasks/user/{user_id}/`
- **Example:** `GET /api/tasks/user/1/`
- **Response (`200 OK`):**
```json
[
    {
        "id": 1,
        "name": "Fix API Bug",
        "description": "Fix the 404 error when accessing /api.",
        "created_at": "2025-03-25T12:00:00Z",
        "status": "Pending"
    }
]

