import imp
from sre_constants import SUCCESS
from flask import Flask,jsonify,request
import csv 
all_movies=[]
with open("movie.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
liked_movies=[]
not_liked_movies=[]
did_not_watched=[]
app=Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"

    })


@app.route("/liked_movie",methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201


@app.route("/unliked_movie",methods=["POST"])
def unliked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201


@app.route("/did_not_watch",methods=["POST"])
def did_not_watch():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watched.append(movie)
    return jsonify({
        "status":"success"
    }),201


if __name__ =="__main__":
    app.run()