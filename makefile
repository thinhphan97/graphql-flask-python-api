
service_build:
	docker-compose build

service_up:
	docker-compose up -d

service_down:
	docker-compose down && docker volume rm postgres_data

service_stop:
	docker-compose stop

service_rm:
	docker-compose rm