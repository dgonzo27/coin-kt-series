# COIN KT Series

This repository contains the example code and documentation for the COIN (Commercial Intelligence) KT (knowledge transfer) series.

## Table of Contents

- [Contributing](#contributing)
- [FastAPI and Pydantic](#fastapi-and-pydantic)
  - [API Frameworks Why](#api-frameworks-why)
  - [API Frameworks What](#api-frameworks-what)
- [SQLAlchemy and Alembic](#sqlalchemy-and-alembic)
  - [SQLAlchemy What and Why](#sqlalchemy-what-and-why)
  - [Alembic What and Why](#alembic-what-and-why)
- [FastAPI Pagination](#fastapi-pagination)
- [Angular Modules](#angular-modules)
- [PAL](#pal)
- [Learn More](#learn-more)

## Contributing

Contributions and suggestions are welcomed. However, there is a level of responsibility placed on the contributor to follow best-practices, provide thorough testing, follow the branching strategy, use the pull request template, and maintain a positive and coachable attitude when receiving feedback or questions on your code. For more details on these responsibilities, please visit the [contributing guide](./CONTRIBUTING.md).

When contributing, you are granting the maintainers of this repository the rights to use your contribution(s).

## FastAPI and Pydantic

**01/26/2024 - FastAPI and Pydantic**.

### API Frameworks Why

Why do we use an API framework and what benefits does it have?

1. Time and Cost Efficiency

   - Faster Development: API frameworks often come with pre-built functionalities and features that can significantly speed up the development process. This allows developers to focus on the unique aspects of their project rather than reinventing the wheel.

   - Cost Savings: Building a custom API can be time-consuming and expensive. Using a framework can save both development time and associated costs.

2. Standardization

   - Consistent Design: API frameworks typically follow standardized design principles and conventions. This ensures a consistent structure across different parts of the API, making it easier for developers to understand and use.

   - Interoperability: Standardized frameworks increase the chances of interoperability between different systems, making it easier to integrate with third-party services.

3. Security

   - Built-in Security Measures: API frameworks often come with built-in security features, such as authentication and authorization mechanisms. Using a well-established framework can reduce the risk of security vulnerabilities compared to rolling out a custom solution.

4. Scalability

   - Scalability Support: Many API frameworks are designed with scalability in mind. They include features that make it easier to scale the application as user demands increase without requiring a complete overhaul of the API.

5. Community Support

   - Community and Documentation: Popular API frameworks often have a large and active community. This means there are more resources, tutorials, and support available. Developers can benefit from the collective knowledge of the community, making problem-solving more efficient.

6. Updates and Maintenance

   - Regular Updates: Frameworks are usually actively maintained and updated by a community or organization. This ensures that the API remains compatible with the latest technologies and standards, reducing the burden on the development team to keep the API up-to-date.

7. Testing and Debugging

   - Testing Tools: API frameworks often come with built-in testing tools and utilities. This can streamline the testing and debugging process, ensuring that the API functions correctly and reliably.

8. Focus on Core Features

   - Reduced Boilerplate Code: Frameworks handle common tasks, such as routing and request handling, reducing the amount of boilerplate code developers need to write. This allows the team to focus more on implementing core features of their application.

### API Frameworks What

What are our needs and requirements for selecting an API framework?

1. Python - we need a Python-based framework since that is the language we are using for COIN's backend.

2. Dependency Injection - we need the ability to inject multiple dependent data sources such as S3, DynamoDB, PostgreSQL, and Redshift (CEDW).

3. Interoperable Serialization - we need the ability to easily model our request and response types whether it be JSON from S3 and Dynamo or SQL from our database or CEDW.

4. Fast and Lightweight - we need our API to be fast and lightweight (small package deployed to a Lambda).

5. Compatible with AWS Services - we need our API to be compatible with our AWS Services (packaged as a Lambda function and middleware for API Gateways).

## SQLAlchemy and Alembic

**02/12/2024 - SQLAlchemy and Alembic**.

### SQLAlchemy What and Why

SQLAlchemy is an open-source SQL toolkit and Object-Relational Mapping (ORM) library for the Python programming language. It provides a set of tools for working with relational databases in Python in a more abstracted and Pythonic way, allowing developers to interact with databases using Python objects rather than writing raw SQL queries.

Some key features of SQLAlchemy include:

- Object-Relational Mapping (ORM): SQLAlchemy allows developers to define Python classes that represent database tables, and instances of those classes can be manipulated and persisted to the database without writing SQL statements directly.

- SQL Expression Language: SQLAlchemy provides a SQL expression language that allows developers to construct SQL queries using Pythonic syntax. This makes it easier to build complex queries dynamically.

- Connection Pooling: SQLAlchemy includes connection pooling functionality, which helps manage and reuse database connections efficiently, improving performance and scalability of applications.

- Database Support: SQLAlchemy supports multiple relational database management systems (RDBMS) including PostgreSQL, MySQL, SQLite, Oracle, and Microsoft SQL Server.

- Transactions and Session Management: SQLAlchemy provides support for managing database transactions and sessions, allowing developers to control the scope and lifespan of database operations.

Overall, SQLAlchemy is a powerful and flexible tool for working with databases in Python, providing developers with the ability to interact with databases at a higher level of abstraction while still retaining the flexibility and power of SQL when needed.

### Alembic What and Why

Alembic is a lightweight database migration tool for SQLAlchemy. It provides a way to generate and manage database schema changes in Python projects, particularly those using SQLAlchemy for database interactions.

Here are some key features of Alembic:

- Schema Migrations: Alembic allows developers to define database schema changes in Python code as migration scripts. These scripts are used to upgrade or downgrade the database schema to match the current version of the application.

- Automatic Generation: Alembic can automatically generate migration scripts by comparing the current state of the database with the current state of the SQLAlchemy models in the project. This helps to streamline the process of creating migration scripts for schema changes.

- Versioning: Alembic maintains a version table in the database to track the current version of the schema. This allows it to determine which migrations need to be applied to bring the database schema up to date.

- Script Management: Alembic provides commands to manage migration scripts, including generating new scripts, applying them to the database, and reverting them if necessary.

- Integration with SQLAlchemy: Alembic is designed to work seamlessly with SQLAlchemy, leveraging its features for database interactions and providing a convenient way to manage schema changes in SQLAlchemy projects.

Overall, Alembic simplifies the process of managing database schema changes in Python projects, providing a reliable and efficient way to keep the database schema in sync with the evolving needs of the application.

## FastAPI Pagination

**02/26/2024 - FastAPI Pagination**.

## Angular Modules

**03/11/2024 - Angular Modules**.

## PAL

**03/25/2024 - PAL**.

## Learn More

To learn more about the technologies used in this application, see the following resources:

- [FastAPI](https://fastapi.tiangolo.com) - the official FastAPI documentation
- [FastAPI Pagination](https://pypi.org/project/fastapi-pagination/) - the official FastAPI Pagination library
- [SQLAlchemy](https://www.sqlalchemy.org) - the official SQLAlchemy documentation
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - the official Alembic documentation
- [pre-commit](https://pre-commit.com) - the official pre-commit documentation
