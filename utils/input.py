import requests


def read_input_from_site(day):
    f = open("./utils/session.txt", "r")
    sesson_id = f.read().strip()
    url = f'https://adventofcode.com/2020/day/{day}/input'
    headers = {'cookie': f'session={sesson_id}'}
    resp = requests.get(url=url, headers=headers)
    return resp.text.strip().split('\n')
