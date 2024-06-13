# Flask Project for sample Smart Inventory Management System

## Folder structure
````
smart_inventory_management/
│
├── build/
│   ├── Dockerfile
│   ├── .env
│   └── SAMPLE.env
│
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── run.py
│   └── requirements.txt
│
└── docker-compose.yml

````


### Building docker image
```
 docker build -t anilprz/sims-flask:v0.0.1 -f build/Dockerfile .
```

### Push image to docker hub
```
docker image push anilprz/sims-flask:v0.0.1
```
