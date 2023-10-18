## Challenge for EdMachina

### Running with docker

#### Pre-requisites:
- docker
- docker compose

#### Steps:
1. Create a file called `.env` with environment variables in the root of the project.
2. Build with `docker compose build`.
3. Run with `docker compose up`.
4. In another terminal run the migrations `docker compose exec character alembic upgrade head`.
5. Run test with `docker compose exec character pytest -vv`. 40% coverage!.

#### How to use: 
- Go to `http://localhost:8000/docs`.
- You can also test the endpoints with your preferred rest client. (Postman/Insomnia).
- Inside the tests directory in the dummy folder is a Postman collection with the endpoints and payload.

#### Environment Variables (.env)
```
ENV=dev
SECRET_KEY=ChallengePi2023
ENGINE="sqlite"
```