# Keyword Search API with Elasticsearch

This project demonstrates the implementation of a keyword-based search API using Elasticsearch, Python, and Flask. The
API enables users to perform document searches based on keywords found within the content. The entire system is
containerized using Docker and orchestrated through Docker Compose.

## Folder Structure

```plaintext
.
├── api_gateway
│   ├── app.py                 # API Gateway application
│   └── Dockerfile             # Dockerfile for API Gateway
├── es_setup.py                # Elasticsearch setup script
├── docker-compose.yml         # Docker Compose configuration
├── requirements.txt           # Python dependencies
└── search_service
    ├── app.py                 # Search Service application
    └── Dockerfile             # Dockerfile for Search Service
```

## Prerequisites

- Docker and Docker Compose are installed on your system.
- Basic understanding of Docker and Elasticsearch.

## Getting Started

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/keyword-search-api.git
   cd keyword-search-api

2. **Running the Services**: Use Docker Compose to run the services. Make sure Docker and Docker Compose are installed
   on your system.

    ```bash
    docker-compose up
    ```

3. **API Documentation**: The API Gateway exposes only one endpoint:

    - `GET /search?keyword=<your_keyword>`: Search for documents containing the specified keyword.

4. **Customization**: You can customize the services, API, and Elasticsearch configurations according to your
   requirements.

### NOTE:

Execute es_setup.py to add files from patent_jsons into your Elasticsearch index named "patents". 
