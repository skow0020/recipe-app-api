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

## Coverage checks
`
docker-compose run --rm app sh -c "coverage report --fail-under=100 -m"
`