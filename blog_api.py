from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory blog storage
blogs = []
next_id = 1

# Get all blogs
@app.route('/blogs', methods=['GET'])
def get_all_blogs():
    return jsonify(blogs), 200

# Get a blog by ID
@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog_by_id(blog_id):
    blog = next((b for b in blogs if b['id'] == blog_id), None)
    if blog:
        return jsonify(blog), 200
    return jsonify({'error': 'Blog not found'}), 404

# Post a new blog
@app.route('/blogs', methods=['POST'])
def create_blog():
    global next_id
    data = request.json
    if not all(k in data for k in ['title', 'description', 'category']):
        return jsonify({'error': 'Missing required fields'}), 400
    blog = {'id': next_id, 'title': data['title'], 'description': data['description'], 'category': data['category']}
    blogs.append(blog)
    next_id += 1
    return jsonify(blog), 201

# Update a blog
@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    data = request.json
    blog = next((b for b in blogs if b['id'] == blog_id), None)
    if not blog:
        return jsonify({'error': 'Blog not found'}), 404
    blog.update({k: v for k, v in data.items() if k in ['title', 'description', 'category']})
    return jsonify(blog), 200

if __name__ == '__main__':
    app.run(debug=True)


