# Flask Project for sample Smart Inventory Management System

Smart Inventory System is a given project name for this Flask api project.

Some of the release map and todos are wriiten in separate file.

## Smart Inventory Management System
### Table of Contents

1. Introduction
2. Project Structure
3. Setup Instructions
4. Configuration
5. Migration
6. Running Application
7. Features
    1. Basic Features
    2. Advanced Features

8. Testing
9. Deployment
10. Contributing
11. License



###  Introduction
Provide a brief overview of the project, its purpose, and its main features.


### Project Structure
Outline the project directory structure for clarity.
```
smart_inventory_management/
├── build/
│   ├── Dockerfile
│   ├── .env
│   └── SAMPLE.env
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── item_routes.py
│   │   │   └── auth_routes.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── item_service.py
│   │   │   └── auth_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   └── security.py
│   ├── config.py
│   ├── run.py
│   └── requirements.txt
└── docker-compose.yml
```


### Setup Instructions
Detailed steps to set up the project locally.

### Prerequisites
- Docker
- Docker Compose
- Python 3.11+

### Installation
- Clone the repository:
    ```
    git clone https://github.com/your_username/smart_inventory_management.git
    cd smart_inventory_management
    ```

- Build the Docker image:
    ```
    docker-compose build
    ```
- Run the Docker container:
    ```
    docker-compose up
    ```

### Configuration
Instructions on how to configure the project using environment variables and configuration files.

### Environment Variables
List and explain the environment variables used in the project.

### Configuration Files
- build/.env: Main configuration file for environment variables.
- build/SAMPLE.env: Sample configuration file for reference.

### Migration

#### Initialize the migration repository
```
docker-compose exec simflask flask db init
```

#### Generate an initial migration
```
docker-compose exec simflask flask db migrate -m "Add SOME model."
```

#### Apply the migration to the database
```
docker-compose exec simflask flask db upgrade
```

### Running the Application
Access the application at http://localhost:5000/ or http://zmysims.com if using docker Traefik.

### Flask REST API

#### Authentication

This API uses JWT (JSON Web Token) for authentication. To use the API, you need to:

1. Obtain a JWT token using the `/auth/login` endpoint.
2. Include the token in the `Authorization` header for all subsequent requests.

### Steps

1. ***Login***

   Send a POST request to `/auth/login` with your username and password to obtain a JWT token.

   ```bash
   curl -X POST "http://zmysims/auth/login" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"username\": \"your_username\", \"password\": \"your_password\"}"

2. ***Response***
    ```json
    {
    "access_token": "your_jwt_token"
    }
    ```
3. ***Use the Token***

    Include the token in the Authorization header for all subsequent requests.

    ```bash
    curl -X GET "http://localhost:5000/items" -H "accept: application/json" -H "Authorization: Bearer your_jwt_token"
    ```

4. ***Swagger Documentation***

    The API documentation is available at `http://zmysims/`. You can enter your JWT token in the top-right corner to authorize your requests as
    `Bearer YOUR-GENERATED-TOKEN-HERE`



### Features

#### Basic Features
- User authentication (login, registration)
- CRUD operations for inventory items
- Search and filter functionality
- Basic inventory management dashboard

#### Advanced Features
- User roles and permissions
- Notifications for low inventory
- Reporting and analytics
- Integration with third-party services (e.g., email notifications, SMS alerts)
- Bulk import/export of inventory data


#### Running Tests
  1. Build and run the Docker container:
    ```
    docker-compose up --build
    ```
  2. Execute the tests:
    ```
    docker exec -it simflask pytest
    ```

### Deployment
Steps to deploy the application to production.

### Docker Hub
1. Log in to Docker Hub:
    ```
    docker login
    ```
2. Build and tag the Docker image:
    ```
    docker build -t anilprz/sims-flask:v0.0.1 -f build/Dockerfile .
    docker tag anilprz/sims-flask:latest
    ```
3. Push the Docker image to Docker Hub:
    ```
    docker push anilprz/sims-flask:v0.0.1
    docker push anilprz/sims-flask:latest
    ```


### Cloud Deployment
- Deploying using image in cloud using Traefik
    ```yml
    services:
        simflaskimage:
            container_name: simflaskimage
            image: anilprz/sims-flask:v0.0.1
            ports:
                - "80:5000"
            env_file:
                - build/.env
            labels:
                - "traefik.enable=true"
                - "traefik.http.routers.app.rule=Host(`SUBDOMAIN.prajapatianil.com`)"
            networks:
                - traefik

    networks:
        traefik:
            external: true
    ```


### How to Contribute
- Fork the repository
- Create a new branch (git checkout -b feature/YourFeature)
- Commit your changes (git commit -m 'Add some feature')
- Push to the branch (git push origin feature/YourFeature)
- Open a pull request

### License
Apache License 2.0


