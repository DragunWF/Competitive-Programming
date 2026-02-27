# https://www.codewars.com/kata/5ea39ab1d8425e0029fcd035/train/python

def ping_pong(sounds: str) -> str:
    sound_list = sounds.split("-")
    mr_ping_score = 0
    mr_pong_score = 0
    first_serve = None
    last_sound = None
    last_bad_shot = None

    for sound in sound_list:
        if sound == "ping" or sound == "pong":
            if last_sound is None:
                first_serve = sound
            last_sound = sound
        elif last_sound:
            last_bad_shot = last_sound
            if last_bad_shot != "ping" and first_serve == "ping":
                mr_ping_score += 1
            elif last_bad_shot != "pong" and first_serve == "pong":
                mr_pong_score += 1
            last_sound, first_serve = None, None

    if mr_ping_score == mr_pong_score:
        return "ping" if last_bad_shot == "pong" else "pong"
    return "ping" if mr_ping_score > mr_pong_score else "pong"


def test() -> None:
    # Expected: ping
    print(ping_pong("ping-pong-ping-pong-bonk-bing-doof"))

    # Expected: pong
    print(ping_pong('pong-ping-pong-donk-pong-ping-pong-donk-pong-ping-pong-doof-pong-ping-donk'))

    # Expected: ping
    print(ping_pong('ping-pong-aaaa-ping-pong-ping-aaaa'))


if __name__ == "__main__":
    test()
