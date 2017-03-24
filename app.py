from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
<<<<<<< HEAD
    return 'Hello Minjar!!!! I have been seen {} times.\n'.format(count)
=======
    return 'Hello Docker Happy Birthday!!! I have been seen {} times.\n'.format(count)
>>>>>>> 67a12ae7d9d66abbb2ec23c6278c10da9fbd0f63

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

