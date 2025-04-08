# Medium Blog Scraper

This is a Flask-based web scraper that extracts blog posts from a given Medium URL. The application scrapes the blog titles and post URLs and returns them in a JSON format.

## Features
- Scrapes Medium blog posts
- Extracts title and post URL
- Provides API access via a simple GET request

## Technologies Used
- Python 3.9
- Flask
- Requests
- BeautifulSoup4
- Docker

## Installation

### Prerequisites
- Docker (for containerized deployment) or Python 3.9+

### Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t medium-scraper .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 medium-scraper
   ```

### Running Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/ahn1305/medium-scraper.git
   cd medium-scraper
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set the Flask app environment variable:
   ```sh
   export FLASK_APP=api.py
   ```
4. Run the Flask application:
   ```sh
   flask run --host=0.0.0.0 --port=5000
   ```

## API Usage
Send a GET request to scrape a Medium blog:
```sh
curl "http://localhost:5000/scrape?url=https://medium.com/example-blog"
```

### Response Format
```json
[
  {
    "pno": 1,
    "title": "Sample Blog Title",
    "url": "https://medium.com/example-blog/post"
  }
]
```

## License
This project is open-source and available under the MIT License.
