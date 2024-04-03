from flask import Flask, jsonify, request
app = Flask(__name__)

keys = ['6764-0878-8007-9688', '04-03', '04-10']

@app.route('/<key>', methods=['get'])
def getconfig(key):
    print(key)
    return jsonify(key)

if __name__ == "__main__":
    app.run()