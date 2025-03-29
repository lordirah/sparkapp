# sparkapp

```
docker-compose up
docker exec irah-spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/main.py
docker compose down --volumes --remove-orphans

# Above will be converted to use makefile
```
