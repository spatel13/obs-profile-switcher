import time

from obswebsocket import obsws, events, requests

host = 'localhost'
port = 4444
password = ''


if __name__ == '__main__':
    ws = obsws(host, port, password)
    ws.connect()

    try:
        # scene_collections = ws.call(requests.ListProfiles())
        # print(scene_collections.getProfiles())

        _ = ws.call(requests.SetCurrentSceneCollection("League Twitch"))
        _ = ws.call(requests.SetCurrentProfile("League"))

        # time.sleep(10)

        # print()

        # scene_coll_name = ws.call(requests.GetCurrentSceneCollection()).getScName()
        # print(f"Scene Collection Name: '{scene_coll_name}'")
        # profile_name = ws.call(requests.GetCurrentProfile()).getProfileName()
        # print(f"Profile Name: '{profile_name}'")


    except KeyboardInterrupt:
        ws.disconnect()
        pass