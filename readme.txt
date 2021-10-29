[build]
docker build -t {tag}:latest .

[run]
docker run --publish 8080:8080 {the tag} or docker-compose up


I made the first problem be a part of the second one. While building a docker container the parser runs 
and stores the data it obtained from xlsx files into different files. Flask uses files created by parser