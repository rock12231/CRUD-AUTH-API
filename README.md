# oodles Assesment
Auth and CRUD API's

#### RUN Project
###### 1. Clone the project
```git clone https://github.com/rock12231/oodles.git```
###### 2. Create a virtual environment
```python -m venv venv```
###### 3. Activate the virtual environment
```venv\Scripts\activate```
###### 4. Install the requirements
```pip install -r requirements.txt```
###### 5. Run the server
```python manage.py runserver```

<br>
<br>

## Authentication & API's
#### POST
###### Login
###### API ```http://127.0.0.1:8000/api/token/```
```json
{
    "email": "user1@gmail.com",
    "password": "user1"
}
 ```
###### Out put

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTg0MjMyMSwiaWF0IjoxNjc5NzU1OTIxLCJqdGkiOiJkN2JlZWM4MThjYzY0ZTU5OTFlMWY3NzQzYWY2NDFhMiIsInVzZXJfaWQiOjN9.rhTvXyRqaOPdHdrUlbgypkXO0uk-Hv5IE1604QkSuxQ",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5NzU2MjIxLCJpYXQiOjE2Nzk3NTU5MjEsImp0aSI6Ijc5ZThkZmM3OTJlMTQyYzRiYTA3OGIxYmRiZjliY2MyIiwidXNlcl9pZCI6M30.XFTQQHuWAHVQq2vqE80bVS9w3AH-ll_iahdfQf6Hmek"
}
```
#### POST
###### Create a User (Register)
###### API ```http://127.0.0.1:8000/api/register/```

```json  
{
    "email": "user1@gmail.com",
    "username": "user1",
    "password": "user1",
    "first_name": "user1",
    "last_name": "user1"
}
  ```

###### Out put
```json
{
    "response": "Successfully registered a new user.",
    "email": "user1@gmail.com",
    "username": "user1",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTg0MjE1MCwiaWF0IjoxNjc5NzU1NzUwLCJqdGkiOiI4NzVlOWM3YjVhNTI0NGM5OTQwNDg5Yjk3Y2ZiYWU3NCIsInVzZXJfaWQiOjR9.TA-EnzA8_RhzncMNKmQl9NQj8pNRz9PxJ3GFKEbyqes",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5NzU2MDUwLCJpYXQiOjE2Nzk3NTU3NTAsImp0aSI6ImQyNjcyODhlODRmYTQxYWRiNGIzODc3MjM2MjI5NWU1IiwidXNlcl9pZCI6NH0.ZRrSzIDlUqABI8i0n9prnlC9RXU1dJa6mPwgup3mlok"
}
 ```

<br>

#### GET
###### Get all designs
###### API ```http://127.0.0.1:8000/api/alldesigns```
###### Out put
```json  
[
    {
        "id": 1,
        "title": "color",
        "description": "desc",
        "creator": "avi",
        "price": 100,
        "creation_date": "2023-03-25",
        "last_update_date": "2023-03-25",
        "tags": "#color",
        "user": 2
    },
    {
        "id": 2,
        "title": "color",
        "description": "desc",
        "creator": "avi",
        "price": 100,
        "creation_date": "2023-03-25",
        "last_update_date": "2023-03-25",
        "tags": "#color",
        "user": 2
    }
] 
  ```

###### Get one designs
###### API ```http://127.0.0.1:8000/api/designs/1```
###### Out put
```json  
[
    {
        "id": 1,
        "title": "color",
        "description": "desc",
        "creator": "avi",
        "price": 100,
        "creation_date": "2023-03-25",
        "last_update_date": "2023-03-25",
        "tags": "#color",
        "user": 2
    }
] 
  ```

<br>
#### POST
###### Create a design
###### API ```http://127.0.0.1:8000/api/designs```

```json  
{
    "email": "user1@gmail.com",
    "username": "user1",
    "password": "user1",
    "first_name": "user1",
    "last_name": "user1"
}
  ```

<br>

#### PUT
###### Update a design
###### API ```http://127.0.0.1:8000/api/design/1```
    
```json  
{
  "title": "color",
  "description": "description",
  "creator": "oodals",
  "price": 1000,
  "tags": "#green",
  "user": 1
}
  ```

###### Out put
```json
{
  "id": 2,
  "title": "color",
  "description": "description",
  "creator": "oodals",
  "price": 1000,
  "creation_date": "2023-03-25",
  "last_update_date": "2023-03-25",
  "tags": "#green",
  "user": 1
}
 ```

<br>

#### DELETE
###### Delete a design
###### API ```http://127.0.0.1:8000/api/design/1```

