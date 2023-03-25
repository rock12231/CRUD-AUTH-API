# oodles
Auth and CRUD API's


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

#### POST
###### Create a design
###### API ```http://127.0.0.1:8000/api/register```

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

#### DELETE
###### Delete a design
###### API ```http://127.0.0.1:8000/api/design/1```

