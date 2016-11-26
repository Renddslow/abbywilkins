import datetime

from flask_login import UserMixin

from peewee import *

DATABASE = MySQLDatabase("abby",host="localhost",
							user="brink",passwd="littleredunicorns")

class BaseModel(Model):
	class Meta:
		database = DATABASE


class Posts(BaseModel):
	post_id = PrimaryKeyField()
	post_title = CharField(index=True)
	post_text = TextField()
	post_image_uri = CharField()
	date_created = DateTimeField(default=datetime.datetime.now())


class Users(BaseModel, UserMixin):
	username = CharField(unique=True, index=True)
	password = CharField()
	first_name = CharField()
	last_name = CharField()
	is_admin = BooleanField()


class Comments(BaseModel):
	comment_id = PrimaryKeyField()
	comment_text = TextField()
	user_id = IntegerField(index=True)
	date_created = DateTimeField(default=datetime.datetime.now())


class Likes(BaseModel):
	like_id = PrimaryKeyField()
	post_id = IntegerField(index=True)
	user_id = IntegerField(index=True)
	date_created = DateTimeField(default=datetime.datetime.now())


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Posts,Users,Comments], safe=True)
	DATABSE.close()
