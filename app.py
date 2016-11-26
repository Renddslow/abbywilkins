from flask import (Flask, g, render_template,
					jsonify, request)

import models

application = Flask(__name__)


@application.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@application.after_request
def after_request(response):
	g.db.close()
	return response

@application.route("/")
def home():
	return render_template("home.html")

@application.route("/upload", methods=['GET','POST'])
def upload():
	return render_template("upload.html")

@application.route("/posts")
def get_posts():
	page = int(request.args.get("page"))
	limit = int(request.args.get("limit"))
	posts = (models.Posts.select()
					.order_by(models.Posts.date_created)
					.paginate(page, limit))
	post_list = []
	for post in posts:
		post_dict = {
			"title": post.post_title,
			"text": post.post_text,
			"image": post.post_image_uri,
			"date_created": post.date_created
		}
		post_list.append(post_dict)
	return jsonify(post_list)

if __name__ == "__main__":
	application.run(host='0.0.0.0')
