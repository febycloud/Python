from flask import Flask,jsonify
from flask_restful import Api,Resource
import requests

route_ping="api/ping"
route_post="api/post"

def create_app(test_config=None):
    app=Flask(__name__)
    api=Api(app)

    class Ping(Resource):
        def get(self):
            return {"success":True},200
    
    class Blog(Resource):
        def get(self):

            #error
            tag_error={"error":"Tags parameter is required"}
            sortby_error={"error":"SortBy parameter is invalid"}
            direction_error={"error":"Sort direction is invalid"}
            other_error={"error":"A problem is happend"}

            #tags
            tag_string=request.args.get("tags",None,str)
            if tag_string is None:
                return tag_error,400
            
            sort_by=request.args.get("sortBy","id")
            if sort_by not in ["id","reads","likes","popularity"]:
                return sortby_error,400

            direction=request.args.get("direction","asc")
            if direction not in ["asc","desc"]:
                return direction_error,400

            tags=tag_string.strip().lower().split(",")

            try:
                data=[]
                for tag in tags:
                    res=request.get(
                        f"https://api.hatchways.io/assessment/blog/posts?tag={tag}."
                    ).json()
                    data+=res["posts"]
                data=set(data)
                print(len(data))

                is_desc=True if direction=="desc" else False
                data=sorted(data,key=lambda x: x[sort_by],reverse=is_desc)
                return {"post":data},200
            except:
                return other_error,400

    api.add_resource(Ping,route_ping)
    api.add_resource(Blog,route_post)

    return app





