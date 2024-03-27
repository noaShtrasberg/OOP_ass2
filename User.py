from Post import PostFactory
from Observer import *


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.myfollowers = ObserverFollowers(self.name)  # my followers
        self.notes = ObserverNotes(self.name)  # like/comment to posts / my notifications
        self.posts = 0
        self.connect = True

    def follow(self, other):
        if self.name != other.name and self.connect:
            if self not in other.myfollowers.followers:
                other.myfollowers.follow_me(self)

    def unfollow(self, other):
        if self in other.myfollowers.followers:
            if self.connect:
                other.myfollowers.unfollow_me(self)

    def publish_post(self, post_type, data, price="", place=""):
        if self.connect:
            self.posts += 1
            new_post = PostFactory.create_post(self, post_type, data, price, place)
            self.myfollowers.update_post()
            print(new_post)
            return new_post

    def print_notifications(self):
        print(self.notes)

    def pass_check(self, password):
        return self.password == password

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {self.posts}, Number of followers: {self.myfollowers.num_of_followers()}"