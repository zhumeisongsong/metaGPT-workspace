from typing import List
from models import User, Photo, Comment, Like, Notification

class UserSerializer:
    def serialize(self, user: User) -> dict:
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'followers_count': user.followers_count,
            'following_count': user.following_count,
            'photos': [photo.id for photo in user.photos],
            'followers': [follower.id for follower in user.followers],
            'following': [following.id for following in user.following],
            'comments': [comment.id for comment in user.comments],
            'likes': [like.id for like in user.likes],
            'notifications': [notification.id for notification in user.notifications]
        }

class PhotoSerializer:
    def serialize(self, photo: Photo) -> dict:
        return {
            'id': photo.id,
            'image_url': photo.image_url,
            'user': photo.user.id,
            'comments': [comment.id for comment in photo.comments],
            'likes': [like.id for like in photo.likes]
        }

class CommentSerializer:
    def serialize(self, comment: Comment) -> dict:
        return {
            'id': comment.id,
            'text': comment.text,
            'user': comment.user.id,
            'photo': comment.photo.id
        }

class LikeSerializer:
    def serialize(self, like: Like) -> dict:
        return {
            'id': like.id,
            'user': like.user.id,
            'photo': like.photo.id
        }

class NotificationSerializer:
    def serialize(self, notification: Notification) -> dict:
        return {
            'id': notification.id,
            'text': notification.text,
            'user': notification.user.id,
            'photo': notification.photo.id
        }
