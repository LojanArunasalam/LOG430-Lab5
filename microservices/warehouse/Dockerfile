FROM python:3.11-slim

# As if you were doing "cd .."
WORKDIR /app

COPY /microservices/warehouse .

# RUN command: like trying to run a linux command
RUN pip install -r requirements.txt

CMD [ "uvicorn", "app:app", "--host 0.0.0.0", "--port 8002", "--reload"]

