# sparkapp

```
# Interim
docker-compose up
docker exec irah-spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/main.py
docker-compose down --volumes --remove-orphans

```
# TODO
- Add pre-commit hooks (lint, formating)
- Makefile complete
- Cluster mode include if possible (Yarn)

# Setup
- Create a requirements.in file and use uv to compile to requirements.txt
  - `uv·pip·compile·requirements.in`
- Dockerfile
  - Install all the packages required for os
  - Set path for hadoop and spark
  - Download the spark image
  - Create a spark-default.conf file to set some conf
  - Create a entrypoint.sh which can help submit the spark application
  - This way of setup we can run the spark app in client mode
    - client mode means that the driver code is running on our machine
- Docker compose
  - spark-master
    - image name
    - entrypoint
    - in volumes mount the folder in repo which will have all the scripts
      - for access failures include `:z`
    - refer the env file for spark conf
  - spark-history-server
  - spark-worker
- Makefile
  - Create a makefile which can do all the command related operations

# Setup cluster mode

- Advantage of this setup
  - scale the worker
  - uses same image for all three container
  - Makefile controlable


