from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_do_follow(True, percentage=50)

    session.set_do_comment(True, percentage=100)


    session.set_comments(["hi @{}, have a look", "Great content @{} have a look", ":heart_eyes: :heart_eyes: :heart_eyes: @{}"])


    session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=30, peak_likes_daily=250,
                                 peak_likes_hourly=30, sleep_after=['likes', 'follows'])


    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    min_followers=150,
                                    min_following=50)

   
    session.like_by_tags(['python3','javascript'], amount=300)

session.end()
