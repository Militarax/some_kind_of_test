[build]
docker build -t {tag}:latest .

[run]
docker run --publish 8080:8080 {the tag} or docker-compose up