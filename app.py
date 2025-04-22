from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/posts')
def get_posts():
    with open('data.json', 'r') as file:
        posts = json.load(file)
    return jsonify(posts)

@app.route('/api/add_post', methods=['POST'])
def add_post():
    new_post = request.get_json()
    with open('data.json', 'r') as file:
        posts = json.load(file)
        posts.insert(0, new_post)
        with open('data.json', 'w') as file:
            json.dump(posts, file, indent=4)
        
        return jsonify({"status": "success"}), 2011


if __name__ == '__main__':
    app.run(debug=True)
