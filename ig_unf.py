Here is a sample code that you can use as a starting point to achieve your goal. This code uses the instaloader library to interact with Instagram. You will need to install this library by running pip install instaloader before running the code.

import instaloader
import time

L = instaloader.Instaloader()

# Login into account
username = 'your_username'
password = 'your_password'
L.context.log(username)
L.load_session_from_file(username)
try:
    L.context.log("Logging in...")
    L.context.username = username
    L.context.password = password
    L.login(username, password)
except Exception as e:
    print(e)

# Get profile information
profile = instaloader.Profile.from_username(L.context, username)

# Get followers and followees
followers = set(profile.get_followers())
followees = set(profile.get_followees())

# Get list of users that you follow but don't follow you back
non_followers = followees - followers

# Unfollow two users every 6 seconds
for user in list(non_followers)[:2]:
    print(f"Unfollowing {user.username}")
    user.unfollow()
    time.sleep(6)