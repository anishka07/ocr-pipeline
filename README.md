### Build the Docker image

```bash 
docker build -t docsumo .   
```

### Run the container

```bash
docker run -p 8000:8000 -e GOOGLE_GEMINI_API="<your-api-key>" docsumo   
```