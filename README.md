__        __   _                    _        _       
\ \      / /__| |__  ___  ___   ___| | _____| |_ ___ 
 \ \ /\ / / _ \ '_ \/ __|/ _ \ / __| |/ / _ \ __/ __|
  \ V  V /  __/ |_) \__ \ (_) | (__|   <  __/ |_\__ \
 _ \_/\_/ \___|_.__/|___/\___/ \___|_|\_\___|\__|___/
| \ | | ___ | |_(_)/ _|_   _                         
|  \| |/ _ \| __| | |_| | | |                        
| |\  | (_) | |_| |  _| |_| |                        
|_| \_|\___/ \__|_|_|  \__, |                        
                       |___/                         


# Websockets Notify

## Introduction
This project demonstrates the use of FastAPI for building a real-time system using WebSockets. The primary purpose is
task and device management with real-time notifications sent over WebSockets whenever tasks are created, updated, or
deleted.

## Project Architecture
The project is built with **FastAPI**, utilizing its asynchronous request handling capabilities, which make it ideal
for WebSockets. The code is structured based on the **Separation of Concerns** principle, where each part has a
clearly defined responsibility.

- **WebSockets** for real-time notifications.
- **Tasks** and **Devices** managed with asynchronous requests.
- **Docker** for easy setup and isolated environment.
- **SQLite** as the lightweight database for storing task and device data.

## Key Features
- **Task Management**: Create, update, delete, and retrieve tasks via REST API with WebSocket notifications for real-time updates.
- **Device Management**: Simulated devices with random online/offline status changes that are broadcast via WebSockets.
- **Real-time WebSocket Communication**: Clients connect to receive live updates.
- **Swagger Documentation**: Auto-generated API docs available at `/docs` for easy exploration and testing of endpoints.

## Why I Chose These Technologies
1. **FastAPI** supports asynchronous operations natively, making it ideal for WebSocket-based real-time applications.
2. **Docker** ensures consistent development and deployment environments.
3. **WebSocket** allows for real-time, bidirectional communication between server and clients.

## How to Run

To get the application up and running quickly using Docker, follow these steps:

### Prerequisites

Ensure that you have Docker installed on your system.

### Build the Docker Image

First, clone this repository to your local machine:

```bash
git clone https://github.com/99994433552/websockets-notify.git
cd websockets-notify
```

Now, build the Docker image:

```bash
docker build -t websockets-notify .
```

This will build the image using the Dockerfile provided in the repository.


### Run the Docker Container

Once the image is built, you can run the container using the following command:

```bash
docker run -p 5050:80 websockets-notify
```

This will start the application and expose it on port 5050 on your local machine.

### Access the Application

After running the container, you can access the application via your browser or any HTTP client like curl or Postman at:

```bash
http://localhost:5050
```

You can use the following endpoints:

- WebSocket connection: Connect to WebSockets at `ws://localhost:5050/ws/{client_id}`
- Task management:
    - `POST /tasks/`: Create a new task.
    - `GET /tasks/`: Retrieve all tasks.
    - `GET /tasks/{task_id}`: Retrieve a specific task.
    - `PUT /tasks/{task_id}`: Update the status of a specific task.\
    - `DELETE /tasks/{task_id}`: Delete a task.
- Device management:
    - `GET /devices`/`: Retrieve all devices.
- Custom Notifications:
    - `POST /notify/`: Send custom notification.

### Automatic API Documentation

FastAPI comes with automatically generated API documentation, which allows you to explore all available endpoints, see their descriptions, and even test them interactively. Once you have the application running, you can access the interactive API docs by navigating to:

- Swagger UI: http://localhost:5050/docs
- Redoc: http://localhost:5050/redoc

These interfaces give you a detailed view of all available endpoints and their parameters, allowing you to make API calls directly from the browser.

### Example WebSocket Interaction

To test the WebSocket notifications, you can use a WebSocket client like `websocat`. Connect to `ws://localhost:5050/ws/{client_id}`, and you will receive real-time notifications for task creation, updates, and device status changes.

```bash
$ websocat ws://localhost:5050/ws/1
{"message": "Device Device U3 is now offline", "url": "/devices/3", "date": "2024-09-14 09:18", "type": "INFO"}
{"message": "Device Device U1 is now offline", "url": "/devices/1", "date": "2024-09-14 09:18", "type": "INFO"}
{"message": "Device Device U1 is now online", "url": "/devices/1", "date": "2024-09-14 09:18", "type": "INFO"}
```

### Stop the Docker Container

To stop the container, find the container ID using `docker ps` and stop it using:

```bash
docker stop <container_id>
```

## FAQ

### 1. Why did you choose FastAPI over Flask or Django?
FastAPI natively supports asynchronous operations and WebSockets, making it highly efficient for real-time
applications. It also provides automatic API documentation.

### 2. How does the system handle WebSocket connections?
Clients connect to the WebSocket endpoint at `/ws/{client_id}` and receive real-time notifications for changes in
tasks and device statuses.

### 3. How are multiple WebSocket connections handled?
The `ConnectionManager` class manages all active WebSocket connections. When tasks or devices are updated, the system
broadcasts notifications to all connected clients.

### 4. How are device statuses updated?
There is a background task that selects a random device and toggles its online/offline status every few seconds. These
changes are broadcast via WebSocket to connected clients.

### 5. How is Docker integrated into the project?
Docker is used to ensure consistent environments for running the application. The Dockerfile allows for building the
project and running it in an isolated container.
