# Movies and Reviews API

This simple Django project uses Docker and can be built via `docker compose build` and run via `docker compose up`

To run initial migrations, run `docker compose run --rm django python manage.py migrate`

This project will serve an API on `localhost:8080`

## Available Endpoints

1. `localhost:8080/api/movies/` -> Retrieve a list of movies or add a new movie
2. `localhost:8080/api/movies/<id>` -> Retrieve, update, or delete a specific movie
3. `localhost:8080/api/movies/<movie_id>/reviews` -> Retrieve a list of reviews for the movie or add a new review
4. `localhost:8080/api/movies?runtime=<runtime_value>` -> Retrieve a list of movies matching the given runtime value
5. `localhost:8080/api/movies?runtime_lt=<runtime_value>` -> Retrieve a list of movies less than the given runtime value
6. `localhost:8080/api/movies?runtime_gt=<runtime_value>` -> Retrieve a list of movies greater than the given runtime value
