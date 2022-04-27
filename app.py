import os
from random import random, seed
from flask import Flask, jsonify, request


app = Flask(__name__)

rseed = os.environ.get("RANDOM_SEED", random())
seed(rseed)

def random_number(from_: int, to_: int):
    if from_ > to_:
        raise ValueError("'from' value cannot be greater than 'to' value!")

    result = random()
    result = from_ + int((to_ - from_) * result)
    return result

@app.route("/")
def random_number_api():
    
    from_ :int = request.args.get("from", 1, type=int)
    to_ :int = request.args.get("to", 1000, type=int)

    result = {}
    status_code = 200
    
    try:
        result["result"] = random_number(from_, to_)
        status_code = 200

    except ValueError as err:
        result["error_message"] = str(err)
        status_code = 400
        
    return jsonify(result), status_code
