## Websockets Notify

This project is a simple FastAPI-based web application that demonstrates the use of WebSockets for real-time notifications. The system includes functionality for managing tasks and devices, with notifications sent over WebSockets when tasks are created, updated, or deleted. Additionally, the application supports random device status updates, which are also broadcasted via WebSockets.

## Features

- WebSocket-based notifications: Real-time communication between the server and clients using WebSockets.
- Task management: Create, update, delete, and retrieve tasks
- Device management: Simulated devices that can randomly change their online/offline status.
- Notifications via WebSockets: Notifications include task creation, task status updates, and device status changes.
- SQLite Database: Data persistence for tasks and devices.

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

## License

This project is licensed under the MIT License.