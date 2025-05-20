### An OCR pipeline that shows the implementation of singleton, factory and strategy design patterns.

### Build the Docker image

```bash 
docker build -t <your_docker_file_name> .   
```

### Run the container

```bash
docker run -p 8000:8000 -e GOOGLE_GEMINI_API="<your-api-key>" <you_docker_file_name>   
```