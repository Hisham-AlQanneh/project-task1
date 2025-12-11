# Employee Management System

## Purpose
A simple web-based employee management system that allows you to add, view, update, and delete employee records. The system includes a dashboard with visualizations for employee data analysis.

## Structure

### Backend (`backend.py`)
- **Framework**: FastAPI
- **Database**: SQLite (`employee.db`)
- **Features**:
  - REST API endpoints for CRUD operations
  - Logging to `app.log`
  - CORS enabled for frontend access

### Frontend (`streamlit.py`)
- **Framework**: Streamlit
- **Features**:
  - Dashboard with employee statistics and charts
  - Form to add new employees
  - Update and delete existing employees

### Database
- **employees** table with fields:
  - employee_id (auto-increment primary key)
  - name
  - department
  - salary
  - hire_date

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| GET | `/employees/{id}` | Get specific employee |
| POST | `/employees` | Add new employee |
| PUT | `/employees/{id}` | Update employee |
| DELETE | `/employees/{id}` | Delete employee |

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the backend**:
   ```bash
   uvicorn backend:app --reload
   ```
   Backend runs on `http://127.0.0.1:8000`

3. **Start the frontend** (in a new terminal):
   ```bash
   streamlit run streamlit.py
   ```
   Frontend opens in your browser automatically

## Usage

### Dashboard
- View all employees in a table
- See average salary
- View employees per department (bar chart)
- See salary distribution (histogram)

### Manage Employees
- **Add**: Fill in employee details and click "ADD"
- **Update**: Select employee ID, edit fields, click "Update"
- **Delete**: Select employee ID, click "Delete"

## Files
- `backend.py` - FastAPI server
- `streamlit.py` - Streamlit frontend
- `employee.db` - SQLite database
- `app.log` - Application logs
- `requirements.txt` - Python dependencies
- `conn.py` - SQL Server connection (unused)
- `*.dockerfile` - Docker configuration (empty)