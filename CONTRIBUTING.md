---
title: Contributing
---

# Contributing

This document provides supporting steps and documentation for developing locally.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development Guide](#local-development-guide)
  - [First Time Setup](#first-time-setup)
  - [Not My First Rodeo](#not-my-first-rodeo)
- [VS Code Typehints](#vs-code-typehints)
- [Docker Related Commands](#docker-related-commands)
- [Git Related Commands](#git-related-commands)

## Prerequisites

Before jumping into the code, there are a few prerequisites.

1. Local development should be done from a UNIX-based machine - use Linux, MacOS, or WSL2 if you're on a Windows machine.

2. GitHub access should be managed through an SSH key in your UNIX environment. If you're unfamiliar with this process [start here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

3. [Node Version Manager](https://github.com/nvm-sh/nvm) should be installed on your machine for managing node versions for current and future maintenance of UI packages. This project is currently using v20.11.0.

   ```sh
   source ~/.nvm/nvm.sh  # activate nvm once installed

   nvm install v20.11.0  # install node

   nvm use v20.11.0  # use node
   ```

4. [Docker Desktop](https://www.docker.com/products/docker-desktop/) should be installed on your machine for local development. If you're on Windows, configure your settings to enable Docker Desktop in WSL2.

5. [pre-commit](https://pre-commit.com/) should be installed globally on your machine for linting and validating your code prior to pushing up to GitHub.

## Local Development Guide

This project uses a variation of [scripts to rule them all](https://github.com/github/scripts-to-rule-them-all).

### First Time Setup

Start here if this is your first time setting up the project!

1. Clone the repository (if this is your first time).

   ```sh
   git clone git@github.com:dgonzo27/coin-kt-series.git
   ```

2. Navigate into the repository directory.

   ```sh
   cd coin-kt-series
   ```

3. Enable pre-commit for this repository.

   ```sh
   pre-commit install
   ```

4. Navigate into the `client` directory and install the node modules.

   ```sh
   cd client && npm install
   cd ..
   ```

5. Setup and run the project from scratch. If the connection to the DB container fails, just run the setup script again.

   ```sh
   scripts/setup
   ```

6. Visit the [website](http://localhost:4200) and [Swagger API docs](http://localhost:8000/docs) to smoke test.

7. Stop the Docker containers.

   ```sh
   scripts/stop
   ```

8. Run the project again without re-building from scratch.

   ```sh
   scripts/start --d

   scripts/stop
   ```

9. Visit the [VS Code Typehints](#vs-code-typehints) section to get your code editor setup for local development.

### Not My First Rodeo

Start here if this isn't your first rodeo!

1. Ensure you have the latest code from the `master` branch.

   ```sh
   git pull origin master
   ```

2. Developing? Checkout to a `features/*` or `bugs/*` branch.

   ```sh
   git checkout -b features/my-new-feature
   ```

3. If there was new code in the `client/package.json` file, be sure to re-install your node modules and rebuild the containers.

   ```sh
   cd client && npm install
   cd ..
   scripts/update
   ```

4. Pickup where you left off if there weren't any changes after pulling the latest code.

   ```sh
   scripts/start --d
   ```

5. If there were changes, wipe the images, and rebuild or simply rebuild the containers.

   ```sh
   # start from scratch
   scripts/clean

   scripts/setup

   # or simply rebuild and start
   scripts/update
   scripts/start --d
   ```

6. Visit the [website](http://localhost:4200) and [Swagger API docs](http://localhost:8000/docs) to smoke test.

7. Stop the Docker containers.

   ```sh
   scripts/stop
   ```

8. Run the project again without re-building from scratch.

   ```sh
   scripts/start --d

   scripts/stop
   ```

## VS Code Typehints

1. From the root directory of this repository in your terminal, create a Python virtual environment.

   ```sh
   python3 -m venv .venv
   ```

2. Activate the virtual environment.

   ```sh
   source .venv/bin/activate
   ```

3. Install the requirements.

   ```sh
   pip install -r ./server/requirements.txt
   ```

4. When opening VS Code, you should be prompted to change the interpreter to your virtual environment. If you aren't prompted you can open your command palette (cmd + shift + p on mac, ctrl + shift + p on windows) and search for "interpreter". The "Python: Select Interpreter" option should appear as you start typing if you have installed the Python VS Code extension supported by Microsoft.

5. When you're finished developing, deactivate your virtual environment.

   ```sh
   deactivate
   ```

## Docker Related Commands

1. Run the containers with logs to your terminal.

   ```sh
   scripts/start # start containers

   ctrl + c  # stop execution in terminal

   scripts/stop # bring down containers
   ```

2. Force a clean rebuild of the Docker images.

   ```sh
   scripts/update --no-cache
   ```

3. Clear Docker system (images/containers) and volume cache.

   ```sh
   scripts/clean
   ```

4. Create a migration after updating a model in `server/api/models/sqlalchemy.py`.

   ```sh
   docker compose exec coin-api alembic revision --autogenerate -m "create some table"
   ```

5. Upgrade database to the latest migration version.

   ```sh
   docker compose exec coin-api alembic upgrade head
   ```

6. Downgrade database to the previous migration version.

   ```sh
   docker compose exec coin-api alembic downgrade -1
   ```

7. Show database migration history.

   ```sh
   docker compose exec coin-api alembic history
   ```

8. Login to the database from your terminal while the containers are running.

   ```sh
   docker compose exec coin-db psql -U postgres

   psql (13.4)
   Type "help" for help.

   postgres=# \c api_dev
   You are now connected to database "api_dev" as user "postgres".

   api_dev=# \dt
               List of relations
   Schema |    Name     | Type  |  Owner
   --------+-------------+-------+----------
   public | items        | table | postgres
   (1 row)

   api_dev=# SELECT * FROM public."items";
   id | name             | price                  | is_offer
   ---+------------------+------------------------+-------------
   1  | Potato           | 0.98                   | False
   (1 row)

   api_dev=# \q
   ```

9. Wipe and recreate migrations from scratch.

   ```sh
   # after deleting the `server/migrations` folder and the `server/alembic.ini` file
   # you can rebuild your containers and init the database migrations
   docker compose build
   docker compose up -d
   docker compose exec coin-api alembic init --template generic migrations

   # update the migrations/env.py file
   # see python example below
   ```

   ```python
   import os  # new
   from logging.config import fileConfig

   from sqlalchemy import engine_from_config
   from sqlalchemy import pool

   from alembic import context

   from api.models import sqlalchemy as models  # new

   # ...
   # target_metadata = None
   target_metadata = models.Base.metadata  # new

   # ...
   def run_migrations_offline() -> None:
      url = os.environ.get("DATABASE_URL")  # new
      # ...

   def run_migrations_online() -> None:
      # connectable = engine_from_config(
      #     config.get_section(config.config_ini_section, {}),
      #     prefix="sqlalchemy.",
      #     poolclass=pool.NullPool,
      # )
      connectable = engine_from_config(
          {
              "script_location": "migrations",
              "prepend_sys_path": ".",
              "version_path_separator": "os",
              "sqlalchemy.url": os.environ.get("DATABASE_URL"),
          },
          prefix="sqlalchemy.",
          poolclass=pool.NullPool,
      )
   ```

   ```sh
   # then create the initial migrations
   docker compose exec coin-api alembic revision --autogenerate -m "initial"

   # upgrade to the latest migration version
   docker compose exec coin-api alembic upgrade head
   ```

## Git Related Commands

1.  List all branches and ensure you're on your recently merged `features/*` or `bugs/*` branch.

    ```sh
    git branch -a
    ```

2.  If you have uncommitted changes you'll want to stash them or undo them.

    ```sh
    git status # show the status of staged and unstaged commits

    git stash # stash any uncommitted changes

    git stash pop # retrieve your stash at a later point - don't run this now it's just an example for later!
    ```

3.  Checkout to the `master` branch.

    ```sh
    git checkout master
    ```

4.  Pull in the latest code from the `master` branch.

    ```sh
    git pull origin master
    ```

5.  Delete your `features/*` or `bugs/*` branch from your local environment.

    ```sh
    git branch -D features/my-new-feature
    ```

6.  Prune any remote branch caching from GitHub.

    ```sh
    git remote prune origin
    ```
