# Grippi Campaign Analytics Dashboard

A full-stack application for displaying marketing campaign analytics data.

## Project Structure

```
.
├── frontend/          # Next.js frontend application
├── backend/           # FastAPI backend application
└── database/          # Database setup scripts
```

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- PostgreSQL
- npm or yarn

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   psql -U your_username -d your_database -f database/setup.sql
   ```

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

- `GET /campaigns` - Returns a list of marketing campaigns

## Database Schema

The `campaigns` table contains the following columns:
- id (INTEGER PRIMARY KEY)
- name (VARCHAR)
- status (VARCHAR)
- clicks (INTEGER)
- cost (DECIMAL)
- impressions (INTEGER)

## Deployment

- Frontend: Deployed on Vercel
- Backend: Deployed on Railway
- Database: PostgreSQL on Railway

## Technologies Used

- Frontend: Next.js, React, TailwindCSS
- Backend: FastAPI, Python
- Database: PostgreSQL
- Deployment: Vercel, Railway 