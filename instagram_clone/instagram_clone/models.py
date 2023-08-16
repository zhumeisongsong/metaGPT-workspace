## models.py

from typing import List

class User:
    def __init__(self, id: int, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.followers_count = 0
        self.following_count = 0
        self.photos = []
        self.followers = []
        self.following = []
        self.comments = []
        self.likes = []
        self.notifications = []

    def register(self, username: str, email: str, password: str) -> None:
        """
        Register a new user with the given username, email, and password.
        """
        pass

    def login(self, username: str, password: str) -> None:
        """
        Log in the user with the given username and password.
        """
        pass

    def logout(self) -> None:
        """
        Log out the user.
        """
        pass

    def follow(self, user: 'User') -> None:
        """
        Follow the given user.
        """
        pass

    def unfollow(self, user: 'User') -> None:
        """
        Unfollow the given user.
        """
        pass

    def upload_photo(self, photo: 'Photo') -> None:
        """
        Upload a new photo.
        """
        pass

    def delete_photo(self, photo: 'Photo') -> None:
        """
        Delete the given photo.
        """
        pass

    def like_photo(self, photo: 'Photo') -> None:
        """
        Like the given photo.
        """
        pass

    def unlike_photo(self, photo: 'Photo') -> None:
        """
        Unlike the given photo.
        """
        pass

    def comment_photo(self, photo: 'Photo', comment_text: str) -> None:
        """
        Comment on the given photo with the given text.
        """
        pass

    def delete_comment(self, comment: 'Comment') -> None:
        """
        Delete the given comment.
        """
        pass

class Photo:
    def __init__(self, id: int, image_url: str, user: User):
        self.id = id
        self.image_url = image_url
        self.user = user
        self.comments = []
        self.likes = []

    def add_comment(self, comment: 'Comment') -> None:
        """
        Add the given comment to the photo.
        """
        pass

    def delete_comment(self, comment: 'Comment') -> None:
        """
        Delete the given comment from the photo.
        """
        pass

    def add_like(self, like: 'Like') -> None:
        """
        Add the given like to the photo.
        """
        pass

    def remove_like(self, like: 'Like') -> None:
        """
        Remove the given like from the photo.
        """
        pass

class Comment:
    def __init__(self, id: int, text: str, user: User, photo: Photo):
        self.id = id
        self.text = text
        self.user = user
        self.photo = photo

class Like:
    def __init__(self, id: int, user: User, photo: Photo):
        self.id = id
        self.user = user
        self.photo = photo

class Notification:
    def __init__(self, id: int, text: str, user: User, photo: Photo):
        self.id = id
        self.text = text
        self.user = user
        self.photo = photo

class Auth:
    def __init__(self):
        self.current_user = None

    def register(self, username: str, email: str, password: str) -> None:
        """
        Register a new user with the given username, email, and password.
        """
        pass

    def login(self, username: str, password: str) -> None:
        """
        Log in the user with the given username and password.
        """
        pass

    def logout(self) -> None:
        """
        Log out the user.
        """
        pass

    def is_authenticated(self) -> bool:
        """
        Check if the user is authenticated.
        """
        pass
