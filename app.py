from flask import Flask, request, jsonify
from newspaper import Article

app = Flask(__name__)

@app.route("/")
def index():
    return "Go to /api/article/?url=<url> to do some extractin'"

@app.route("/api/article")
def article():
    url = request.args.get('url')
    if url is None:
        return "Please provide the url (?url=[your url])"

    article = Article(url=url)
    article.download()
    article.parse()
    # article.nlp()
    return jsonify(url=url,
                   title=article.title,
                   authors=article.authors,
                   description=article.meta_description,
                   body=article.text,
                   image=article.top_image,
                   images=article.images,
                   images_sizes=article.image_sizes,
                   videos=article.movies,
                   published=article.published_date,
                   meta=article.meta_data)

if __name__ == '__main__':
    app.run(debug=True)
