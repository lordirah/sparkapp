# sparkapp

```
docker-compose up
docker exec irah-spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/main.py
docker compose down --volumes --remove-orphans

# Above will be converted to use makefile
```

- Add pre-commit hooks (lint, formating)
- Makefile complete
- Cluster mode include if possible (Yarn)
