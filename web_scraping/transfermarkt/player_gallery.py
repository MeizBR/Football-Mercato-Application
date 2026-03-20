import requests

def get_player_gallery(player_id, headers):
    player_gallery_url = "https://tmapi-alpha.transfermarkt.technology/player/" + str(player_id) + "/gallery"

    player_gallery_response = requests.get(
        player_gallery_url,
        headers=headers
    ).json()

    value = {}
    values = []

    gallery_images = player_gallery_response["data"]["images"]

    for image in gallery_images:
        value = {
            "image_title": image["title"],
            "image_url": image["url"],
        }

        values.append(value)

    return values