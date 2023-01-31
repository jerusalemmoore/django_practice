from .models import Post

# retrieve all of users posts including their own as well as the posts of their followers
def retrieveAllPosts(user):
    following = user.following.all()
    # users posts
    posts = Post.objects.filter(user=user)
    followingPosts = Post.objects.none()
    for follower in following:
        otherPosts = Post.objects.filter(user=follower.following)
        followingPosts = followingPosts|otherPosts
    allposts = (posts|followingPosts).order_by('-pub_date')
    return allposts
