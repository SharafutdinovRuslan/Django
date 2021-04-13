import requests
from datetime import datetime


def get_user_id(token, user_name):
    url = 'https://api.vk.com/method/users.get'
    r = requests.get(url=url,
                     params={
                         'v': '5.71',
                         'access_token': token,
                         'user_ids': user_name
                     })

    return r.json().get('response')[0].get('id')


def get_friends_list(token, user_id) -> list:
    url = 'https://api.vk.com/method/friends.get'
    r = requests.get(url=url,
                     params={
                         'v': '5.71',
                         'access_token': token,
                         'user_id': user_id,
                         'fields': 'bdate'
                     })

    return r.json().get('response').get('items')


def calc_age(user_name):
    token = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    ages_map = dict()

    uid = get_user_id(token=token, user_name=user_name)
    friends = get_friends_list(token=token, user_id=uid)
    now = datetime.now()

    for friend in friends:
        if 'bdate' in friend:
            try:
                age = datetime.strptime(friend.get('bdate'), '%d.%m.%Y')
            except ValueError:
                continue

            ages_map[now.year - age.year] = ages_map.get(now.year - age.year, 0) + 1

    answer = list(ages_map.items())
    answer.sort(key=lambda x: (-x[1], x[0]))

    return answer


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
