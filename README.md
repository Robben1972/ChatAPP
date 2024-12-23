# Full-Stack Project

This repository contains a full-stack web application with the following structure:

- **Frontend**: A React-based single-page application (SPA).
- **Backend**: A FastAPI server providing RESTful APIs.

## Features

- Real-time chat integration using [ChatEngine.io](https://chatengine.io).
- Frontend built with React and Vite.
- Backend built with FastAPI.

## Project Structure

```
project/
├── frontend/         # React project
│   ├── src/           # Source code
│   ├── public/        # Static files
│   └── node_modules/  # Dependencies
├── backend/          # FastAPI project
    ├── app/           # Application code
    ├── main.py        # Entry point for FastAPI
```

## Prerequisites

1. [Node.js](https://nodejs.org/) and npm for the frontend.
2. Python 3.9+ and pip for the backend.
3. Register on [ChatEngine.io](https://chatengine.io) to get your `PROJECT_ID` and `PRIVATE_KEY`.

## Setup

### 1. Clone the repository
```bash
git clone git@github.com:Robben1972/ChatAPP.git
cd project
```

### 2. Frontend Setup

Navigate to the `frontend` folder and install dependencies:
```bash
cd frontend
npm install
```

Create a `.env` file in the `frontend` directory and add your ChatEngine project ID:
```
VITE_CHAT_ENGINE_PROJECT_ID=XXXX
```
Replace `XXXX` with your actual `PROJECT_ID` from ChatEngine.io.

Start the React development server:
```bash
npm run dev
```

### 3. Backend Setup

Navigate to the `backend` folder and set up a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate   # For Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Update the `PRIVATE_KEY` in `main.py` with your ChatEngine `PRIVATE_KEY`:

```python
# main.py
PRIVATE_KEY = "your_private_key"
```

Start the FastAPI server:
```bash
uvicorn main:app --reload --port 3001
```

### 4. Environment Variables

Create a `.env` file in the `backend` directory and include:
```
PRIVATE_KEY=your_private_key
```

Replace `your_private_key` with your ChatEngine `PRIVATE_KEY`.

### 5. Access the Application

- Frontend: Visit [http://localhost:5173](http://localhost:5173) (React default Vite port).
- Backend: Visit [http://localhost:3001](http://localhost:3001) (FastAPI default port).

## ChatEngine Setup

1. Register on [ChatEngine.io](https://chatengine.io).
2. Create a new project and note the `PROJECT_ID` and `PRIVATE_KEY`.
3. Update the `.env` files for both the frontend and backend with these values.
