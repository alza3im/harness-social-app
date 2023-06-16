# harness-social-app

## Project prereq

Make sure you have Docker installed and running and docker-compose installed on your machine.

### Brief Description on Tasks Done


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

Use postman to hit the endpoint(s)

Example url: 

http://0.0.0.0:8000/api/signup/


Example request: 

NOTE: You might have an issue with migrations not running.

Incase that happens open a new terminal and log in to the Django container and manually migrate:

```
$ docker-compose exec django bash
app# python3 src/manage.py migrate
```
