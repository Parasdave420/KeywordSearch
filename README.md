# Keyword Search API with Elasticsearch

This project demonstrates the implementation of a keyword-based search API using Elasticsearch, Python, and Flask. The
API enables users to perform document searches based on keywords found within the content. The entire system is
containerized using Docker and orchestrated through Docker Compose.

## Folder Structure

```plaintext
.
└── search_service
   ├── app.py                    # Search Service application
   ├── docker-compose.yml        # Docker Compose configuration
   ├── Dockerfile                # Dockerfile for Search Service
   ├── es_setup.py               # Elasticsearch setup script
   └── requirements.txt          # Python dependencies
```

## Prerequisites

- Docker and Docker Compose are installed on your system.
- Basic understanding of Docker and Elasticsearch.

## Getting Started

1. **Clone this repository**:

   ```bash
   git clone https://github.com/Parasdave420/KeywordSearch.git
   cd search_service

2. **Running the Services**: Use Docker Compose to run the services. Make sure Docker and Docker Compose are installed
   on your system.

    ```bash
    docker-compose up
    ```

3. **API Documentation**: The API Gateway exposes following endpoint:

    - `GET /search?keyword=<your_keyword>&limit=<limit_of_output>`: Search for documents containing the specified keyword.
      - It has two query parameters:
        1. **keyword**: The keyword you want to search. (Required parameter.)
        2. **limit**: Maximum records you want as output. (Optional parameter. Default value is set to 5.)

4. **URL with test**: 
   `http://localhost:5000/search?keyword=Panepinto&limit=10`
   Hit the above URL in postman or browser.
