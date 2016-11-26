from flask import (Flask, g, render_template,
					jsonify, request)

import models
import forms

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
@application.route("/<int:page>")
def home(page=1):
	limit = 20
	posts = (models.Posts.select()
					.order_by(models.Posts.date_created)
					.paginate(page, limit))
	post_list = []
	for post in posts:
		post_dict = {
			"id": post.post_id,
			"title": post.post_title,
			"text": post.post_text,
			"image": post.post_image_uri,
			"date_created": post.date_created
		}
		post_list.append(post_dict)
	return render_template("home.html", posts=post_list)

@application.route("/upload", methods=['GET','POST'])
def upload():
	form = forms.Upload()
	return render_template("upload.html", form=form)


if __name__ == "__main__":
	application.run(host='0.0.0.0')
