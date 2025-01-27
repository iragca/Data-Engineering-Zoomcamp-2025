# Question 1

The Dockerfile in this repo prints out the pip version when building and running
```bash
docker build -t q1
docker run -it q1
```

# Question 2

> Answer: db:5432

The `db:` in the docker-compose file implicitly names this service's hostname. Since they are on the same network, there is no need to use the host mapping to connect to the socket of the service, so it is `5432`.

# Questions 3 - 5

Answers are found within in this directory, the jupyter notebook named `eda.ipynb`.