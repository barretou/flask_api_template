import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True

from flask import jsonify
from server import create_app



app = create_app()

# Routes
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello from flask"})

if __name__ == '__main__':
    app.run(debug=True)
