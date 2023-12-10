FROM python:3.10-slim-buster           
WORKDIR /app                          
COPY . /app/                        
RUN pip install -r requirements.txt   
EXPOSE 5000                            
CMD ["python", "app.py"]             

# Docker build command: docker build -t docker_example_1 .    
# Docker run command: docker run -d -p 5001:5000 docker_example_1