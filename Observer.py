class ObserverNotes:
    def __init__(self, name):
        self.name = name
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

    def like_post(self, like_to):
        like_to.notes.add_notification(f"{self.name} liked your post")
        print(f"notification to {like_to.name}: {self.name} liked your post")

    def comment_post(self, comm_to, comment):
        comm_to.notes.add_notification(f"{self.name} commented on your post")
        print(f"notification to {comm_to.name}: {self.name} commented on your post: {comment}")

    def __str__(self):
        notes = f"{self.name}'s notifications:"
        for notification in self.notifications:
            notes += "\n" + notification
        return notes


class ObserverFollowers:
    def __init__(self, name):
        self.name = name
        self.followers = []  # followers - users

    def follow_me(self, follower):
        self.followers.append(follower)
        print(f"{follower.name} started following {self.name}")

    def unfollow_me(self, unfollower):
        self.followers.remove(unfollower)
        print(f"{unfollower.name} unfollowed {self.name}")

    def num_of_followers(self):
        return len(self.followers)

    def update_post(self):
        for follower in self.followers:
            follower.notes.add_notification(f"{self.name} has a new post")

    def update_discount(self, new_price):
        print(f"Discount on {self.name} product! the new price is: {new_price}")

    def update_sold(self):
        print(f"{self.name}'s product is sold")
