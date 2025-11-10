from flask import Flask, render_template, jsonify, request, send_from_directory
import os, json, datetime
BASE = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE, 'data', 'courses.json')
os.makedirs(os.path.join(BASE, 'data'), exist_ok=True)
if not os.path.exists(DATA_FILE):
    demo = [
        {"id":1,"title":"Complete Python Bootcamp","platform":"Udemy","category":"Programming","price":"Paid","rating":4.7,"url":"https://example.com/python-bootcamp","description":"Hands-on Python course for beginners to advanced."},
        {"id":2,"title":"AI For Everyone","platform":"Coursera","category":"AI","price":"Paid","rating":4.6,"url":"https://example.com/ai-for-everyone","description":"Non-technical intro to AI and its applications."},
        {"id":3,"title":"Web Design for Beginners","platform":"Skillshare","category":"Design","price":"Freemium","rating":4.4,"url":"https://example.com/web-design","description":"Practical web design fundamentals and projects."}
    ]
    with open(DATA_FILE, 'w') as f:
        json.dump(demo, f, indent=2)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/courses', methods=['GET'])
def list_courses():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/courses', methods=['POST'])
def add_course():
    payload = request.json or {}
    required = ['title','platform','category','price','url','description']
    if not all(k in payload for k in required):
        return jsonify({'error':'missing fields'}), 400
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    new_id = max([c.get('id',0) for c in data] or [0]) + 1
    payload['id'] = new_id
    payload['rating'] = float(payload.get('rating') or 0)
    payload['added'] = datetime.datetime.utcnow().isoformat() + 'Z'
    data.insert(0, payload)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    return jsonify(payload), 201

@app.route('/static/<path:fname>')
def static_files(fname):
    return send_from_directory(os.path.join(BASE,'static'), fname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
