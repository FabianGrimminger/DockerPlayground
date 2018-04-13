#official Python runtime
FROM python:3.6-slim

#working directory is /app
WORKDIR /app

#copy everything from current directory to /app
ADD . /app

#install needed requirements
RUN pip install -r requirements.txt

#Make port 8080 available to outside
EXPOSE 8080

#Run myapp
CMD ["python", "myapp.py"]
