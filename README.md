Sensor Data Web Application
==
This web application uses Vue.js to display data from sensors through a Django backend API. The backend API is delivered through Docker and runs on port 8080.

Installation
--
To install and run the application, follow these steps:

    Install Docker on your computer.
    Open the root folder in a terminal or command prompt.
    Run the command docker-compose up to start the Docker containers.

Once the containers are running, you can access the Vue.js application at the following endpoints:

    http://localhost:8080/api/table
    http://localhost:8080/api/metrics
    http://127.0.0.1:8080/api/units
    http://127.0.0.1:8080/api/measurements

The tables can be sorted by clicking/double-clicking on column name

You can also access the following endpoints for the backend API:

    http://127.0.0.1:8000/api/sensors/
    http://127.0.0.1:8000/api/metrics/
    http://127.0.0.1:8000/api/units/
    http://127.0.0.1:8000/api/measurements/
    http://127.0.0.1:8000/api/sensors/int:sensor_id/

Additional information
--

Database was populated by creating a load_data.py script.
python manage.py shell
```
from djangovue.load_data import load_sensor_types, load_metrics, load_sensors
load_sensor_types()
load_metrics()
load_sensors()
```

