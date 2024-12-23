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
    └── .env           # Environment variables
```

## Prerequisites

1. [Node.js](https://nodejs.org/) and npm for the frontend.
2. Python 3.9+ and pip for the backend.
3. Register on [ChatEngine.io](https://chatengine.io) to get your `PROJECT_ID` and `PRIVATE_KEY`.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-repo.git
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
uvicorn main:app --reload
```

### 4. Environment Variables

Create a `.env` file in the `backend` directory and include:
```
PRIVATE_KEY=your_private_key
```

Replace `your_private_key` with your ChatEngine `PRIVATE_KEY`.

### 5. Access the Application

- Frontend: Visit [http://localhost:5173](http://localhost:5173) (React default Vite port).
- Backend: Visit [http://localhost:8000](http://localhost:8000) (FastAPI default port).

## ChatEngine Setup

1. Register on [ChatEngine.io](https://chatengine.io).
2. Create a new project and note the `PROJECT_ID` and `PRIVATE_KEY`.
3. Update the `.env` files for both the frontend and backend with these values.

## Scripts

- **Frontend**
  - `npm run dev`: Start the development server.
  - `npm run build`: Build the application for production.
  - `npm run preview`: Preview the production build.

- **Backend**
  - `uvicorn main:app --reload`: Start the FastAPI server in development mode.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
