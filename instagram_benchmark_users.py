import requests

def get_benchmark_users(instagramId, access_token, username):
    instagram = requests.get(
        f'https://graph.facebook.com/v7.0/{instagramId}?fields=business_discovery.username({username}){{followers_count,follows_count,media_count,username,profile_picture_url}}&access_token={access_token}'
    ).json()
    instagram = instagram["business_discovery"]
    return instagram

def data_Post_to_Bubble(instagram):
    BubbleApiToken = '3f45ca57f3c6e093a05766ba8708120d'
    UserStorageAPI = f'https://ghanins.bubbleapps.io/version-test/api/1.1/obj/BenchMarkUserStorage?api_token={BubbleApiToken}'

    id = instagram['id']
    followers = instagram['followers_count']
    follows = instagram['follows_count']
    mediaCount = instagram['media_count']
    username = instagram['username']
    profile_picture = instagram['profile_picture_url']

    PostData = {
        "followerCount": followers,
        "followsCount": follows,
        "mediaCount": mediaCount,
        "username": username
    }
    requests.post(UserStorageAPI, PostData)

if __name__ == '__main__':
    s3token = 'EAAKnCuyATroBAASs7SQAg9NdiZChumFZCHsf4s9e2l9XsAdpDv79PjGpFSPzM2kur6ixl9UyOH1zfIEuUhHarO0vlBZBCDu7Ocl1681Iw6DeeGEBpb62nIlygQJwwkKiJWAZCaHdqbwcPvMPRUHeg3YPNUOOouNCBmQWv5ITZCdbNqzXL9CmE'
    instagramId = 17841432104009484
    users = ['mono_cosme', 'aloa_used']

    for user in users:
        DataInstagram = get_benchmark_users(instagramId, s3token, user)
        data_Post_to_Bubble(DataInstagram)

