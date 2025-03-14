# Medium Blog Scraper

This is a Flask-based web scraper that extracts blog posts from a given Medium URL. The application scrapes the blog titles, descriptions, and post URLs and returns them in a JSON format.

## Features
- Scrapes Medium blog posts
- Extracts title, description, and post URL
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
   git clone https://github.com/your-repo/medium-scraper.git
   cd medium-scraper
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```sh
   python app.py
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
    "description": "Short blog description.",
    "url": "https://medium.com/example-blog/post"
  }
]
```

## License
This project is open-source and available under the MIT License.

