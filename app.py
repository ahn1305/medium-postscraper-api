import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def extract_title_from_url(url):
    # Get the last part of the path from the URL
    path = urlparse(url).path
    # Split the path by '-' and remove the last element (which is usually the post ID)
    parts = path.strip('/').split('-')[:-1]
    # Capitalize and join the words to form the title
    title = ' '.join(word.capitalize() for word in parts)
    return title


def scrape_medium_blog(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch the webpage"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    main_container = soup.find("div", class_="l ae")
    
    if not main_container:
        return {"error": "No posts found inside the main container"}
    
    articles = main_container.find_all("article")
    data = []
    
    for index, article in enumerate(articles, start=1):
        url_tag = article.find("div", {"data-href": True})
        post_url = url_tag["data-href"] if url_tag else "No URL found"

        # title_tag = article.find("h2", class_="bf lp lq lr ls iu lt lu lv lw iz lx jb jc ly lz jf ma mb mc md me mf mg mh mi mj jq jr js jt ju bk")
        title = extract_title_from_url(post_url) if post_url else "No title found"

        # description_tag = article.find("h3", class_="bf b gf z jq ml jr js mm jt ju ds")
        # description = description_tag.get_text(strip=True) if description_tag else "No description found"

       

        data.append({
            "pno": index,
            "title": title,
            "url": post_url
        })
    
    return data

@app.route("/scrape", methods=["GET"])
def scrape_api():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400
    
    result = scrape_medium_blog(url)
    return jsonify(result)
