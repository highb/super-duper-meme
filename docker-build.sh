#!/bin/sh

docker build -t super-duper-meme_frontend:latest frontend/
docker tag super-duper-meme_frontend:latest localhost:5000/super-duper-meme_frontend:latest
docker build -t super-duper-meme_api:latest api/
docker tag super-duper-meme_api:latest localhost:5000/super-duper-meme_api:latest
