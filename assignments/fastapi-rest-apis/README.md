# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework. In this assignment, you will create endpoints for managing a simple resource and practice request handling, validation, and HTTP response design.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI app and create core endpoints for a simple resource such as books, tasks, or students.

#### Requirements
Completed program should:

- Create a FastAPI app instance in Python.
- Implement a root endpoint (`GET /`) that returns a welcome JSON message.
- Implement `GET /items` to return a list of items.
- Implement `GET /items/{item_id}` to return one item by ID.
- Return clear error responses when an item ID does not exist.


### 🛠️ Add Data Validation and Write Operations

#### Description
Enhance the API by accepting request bodies with validation and supporting creation and updates.

#### Requirements
Completed program should:

- Define a Pydantic model for item input validation.
- Implement `POST /items` to create a new item.
- Implement `PUT /items/{item_id}` to update an existing item.
- Return appropriate HTTP status codes for success and error cases.
- Keep in-memory data structure updates consistent after create and update operations.
