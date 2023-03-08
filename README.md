# recipe-app-api
admin user admin@example.com, password


## Linting
`
docker-compose run --rm app sh -c "flake8"
`

## Run tests 
`
docker-compose run --rm app sh -c "coverage run --source='.' --branch manage.py test"
`

## Spin up docker
`
docker-compose up
`

Documentation locally served at http://127.0.0.1:8000/api/docs/

## Coverage checks
`
docker-compose run --rm app sh -c "coverage report --fail-under=100 -m"
`