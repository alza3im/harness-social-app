# harness-social-app

### Brief Description on Tasks Done

A simple REST API based social network in Django where Users can sign up and login, create/delete/edit/read text posts, as well as, like, and unlike other Users’ posts. 

Once signed up successfully, data enrichment is performed asynchronously via a Celery task, where the geolocation data of the IP that the signup originated from is fetched from abstractapi's api, with multiple retries setup for requests towards it.


The following API endpoints were implemented :  
-  user signup
-  ser login
-  get user data
-  Post CRUD
-  Post like/unlike 


#### Features
1. Blog Management: The application allows users to create, update, and delete blog posts. It provides endpoints for creating new posts, updating existing posts, and retrieving post details, in addition to liking and unliking posts
2. User Management: Users can sign up, log in. The system utilizes JWT authentication to handle user authentication.
3. Celery and Redis Integration: Celery is used as a task queue to handle asynchronous tasks such as fetching IP geolocation data. Redis is used as a message broker to facilitate communication between the Django application and Celery workers.
4. PostgreSQL Database: The project utilizes PostgreSQL as the database management system. PostgreSQL is known for its reliability, stability, and advanced features. It provides ACID compliance, ensuring data integrity, and offers scalability options for large-scale applications. The seamless integration with Django allows for efficient data modeling and querying using the Django ORM.
5. Basic tests were written for SignUpView as a POC
6. Basic serializers were used to validate the data.


### Project prereq

Make sure you have Docker installed and running and docker-compose installed on your machine.


### Steps to get started
1. Clone the repo:
```
git clone https://github.com/alza3im/harness-social-app
```

2. Cd into the project:
```
cd harness-social-app 
```

3. Run the app:
```
docker-compose up
```
App should be running on http://0.0.0.0:8000/


### API endpoints

1. User Managment and JWT Authentication
```
api/ signup/ [name='signup']
api/ login/ [name='login']
api/ token/ [name='token_obtain_pair']
api/ token/refresh/ [name='token_refresh']

```
2. Post Crud and Like/Unlike
```
post/ new/ [name='post-create']
post/ <int:post_id>/update/ [name='post-update']
post/ <int:post_id>/delete/ [name='post-delete']
post/ <int:post_id>/ [name='post-detail']
post/ <int:post_id>/like/ [name='post-like']

```


Sample request: 

```
curl -X POST -H "Content-Type: application/json" -d '{
    "email":"khalil@harness.com",
    "password":"1234",
    "name": "Hire me"
}' http://localhost:8000/api/signup/
```


#### Note 1 :
Most of the endpoints are protected, so if you want to hit them, you should get your tokens first via :

```
curl -X POST -H "Content-Type: application/json" -d '{
    "email":"khalil@harness.com",
    "password":"1234",
}' http://localhost:8000/api/token/
```


#### Note 2

You might have an issue with migrations not running.

In case that happens open a new terminal and log in to the Django container and manually migrate:

```
$ docker-compose exec django bash
app# python3 src/manage.py migrate
```

### To do :

There's still a lot to be considred to do for this application to be production ready, 
the following is a simple to do list:

1. Clean up and environment variables and secrets and 'securely' set up different envs like prod,stagin and dev via bash scripts
2. Finish writing tests for all views
3. Add Holiday Calendar Celery Task, similar to the fetch_ip_geolocation_data() task
4. Setup proper GithubActions ci/cd pipelines for linting, running tests, formatting, running the app
5. Deploy App to AWS ECS
