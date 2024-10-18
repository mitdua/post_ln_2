# FastAPI Project - Comparison Between Synchronous and Asynchronous Code

This project is a small application built with **FastAPI** to demonstrate the difference in performance between using **synchronous** and **asynchronous** code when performing multiple concurrent HTTP requests.

The objective is to make 100 requests to a simulated API and compare the execution time and efficiency between both forms of programming.

## Requirements

- Python 3.10 or higher
- **FastAPI** for the backend (`pip install fastapi`)
- **Uvicorn** as the ASGI server (`pip install uvicorn`)
- **httpx** for making asynchronous HTTP requests (`pip install httpx`)

## Installation

### Clone the repository:
```bash
git clone git@github.com:mitdua/post_ln_2.git
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Start the FastAPI server
```bash
uvicorn main:app --reload
```

### Or Using Docker Compose File (recommended)
```bash
docker compose up --build
```

## Usage Example

### Synchronous requests
curl http://127.0.0.1:8000/task_sync

### Asynchronous requests
curl http://127.0.0.1:8000/task_async


### Measure the time for synchronous requests
time curl http://127.0.0.1:8000/task_sync

### Measure the time for asynchronous requests
time curl http://127.0.0.1:8000/task_async