# MozioAPP

Access the app at: 

## Setting up the application

Rename the file `sample._env` to `.env`
Insert your environment information:

```bash    
    DB_NAME=<your database name />    
    DB_USER=<your database user />    
    DB_PASSWORD=<your database password />    
    DB_HOST=<your container IP />    
    DB_PORT=5432
```

Create the file **app/mozioapp/settings_env.py** and add your environment configurations.
(You can use `app/mozioapp/settings_env__sample.py` as a base to create your configuration file)

## Running the application

Run the application with the command:

```bash
python app/manage.py runserver
```

If you prefer to use Docker, run:

```bash
docker compose up --build
```

Point your browser to: http://localhost:8000/api/doc - to get the api documentation.


You might find it useful to check the application logs ;-)
To free the terminal, use the `-d` flag.

## Migrating to the UV package manager

To use the UV package manager:

1. Install UV: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
2. Execute

```bash
uv sync --locked
```

In case you need add a package, use:

```bash
uv add <package name />
```

UV will create a virtual environment in the project folder (`.venv`). To activate the environment, run:

```bash
source .venv/bin/activate
```

To learn more about UV vs PIP:
[https://docs.astral.sh/uv/guides/migration/pip-to-project/](https://docs.astral.sh/uv/guides/migration/pip-to-project/)

---
