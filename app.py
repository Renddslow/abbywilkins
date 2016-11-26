from flask import (Flask, g, render_template,
					jsonify, request)
from flask_login import (LoginManager, UserMixin, login_required, login_user,
						logout_user, current_user)

import models
import forms

application = Flask(__name__)
application.secret_key = "THIS_IS_A_TEST_KEY_FOR_GITHUB"

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	try:
		models.Users.get(user_id)
		return models.Users
	except models.DoesNotExist:
		return None

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
