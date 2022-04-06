from .base_model import Model
from app.accessors.follower_accessor import FollowerAccessor


class Follower(Model):

    def __init__(self, followee_email, follower_email):
        self.followee_email = followee_email
        self.follower_email = follower_email

    def persist_follow_link(self):
        FollowerAccessor().create_follow_link(self)
