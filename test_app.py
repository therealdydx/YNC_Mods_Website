import requests

url = 'http://127.0.0.1:8080'


def test_create_review():
    data = {
        'course_name': 'Intro to Python',
        'course_code': 'YSC2221',
        'professor': 'Yeo Kheng Meng',
        'year': '2022',
        'rating': '5',
        'workload': '5',
        'grading': '5',
        'review': 'wow'
    }
    res = requests.post(url + '/create_review/', data, allow_redirects=True)
    if res.status_code == 200:
        print('create_review passed')
    else:
        print('create_review failed')


def test_delete_review():
    # Assumes new database and one review exists
    data = {'review_id': '1'}
    res = requests.post(url + '/delete_review/', data, allow_redirects=True)

    if res.status_code == 200:
        print('delete_review passed')
    else:
        print('delete_review failed')


def test_get_list():
    res = requests.get(url + '/list_reviews/')
    if res.status_code == 200:
        print('get_list passed')
    else:
        print('get_list failed')


if __name__ == '__main__':
    test_create_review()
    test_get_list()
    test_delete_review()
