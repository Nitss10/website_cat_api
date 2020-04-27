from flask import Flask
from initialize import kmeans,X,labels,centroids,modelg,titles,l
from flask_cors import CORS, cross_origin

app = Flask(__name__)
from get_result import finalFunction
cors = CORS(app)
app.config['CORS_HEADERS'] = '*'

@app.route('/<path:url>')
@app.route('/')
@cross_origin()
def result_url(url=''):
    return finalFunction(url)

if __name__ == '__main__':
    app.run()