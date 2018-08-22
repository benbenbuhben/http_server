import requests as req


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000')
    assert '<html><body><h1>Hello world</h1></body></html>' == str(response.text)
    assert 'Hello world' in str(response.text)


def test_server_get_returns_404_on_bad_path():
    response = req.get('http://127.0.0.1:5000/dfjhbvdjkf')
    assert response.status_code == 404


def test_server_post_returns_404_on_bad_path():
    response = req.post('http://127.0.0.1:5000/dfjhbvdjkf')
    assert response.status_code == 404


def test_server_get_cow_route_returns_400_without_query():
    response = req.get('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_server_post_cow_route_returns_400_without_query():
    response = req.post('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_server_get_cow_returns_a_talking_steggy():
    response = req.get('http://127.0.0.1:5000/cow?msg=hi')
    expected = ''' ____
                < hi >
                ----
                \                             .       .
                \                           / `.   .' "
                \                  .---.  <    ><    >  .---.
                \                 |    \  \ - ~ ~ - /  /    |
                        _____          ..-~             ~-..-~
                        |     |   \~~~\.'                    `./~~~/
                    ---------   \__/                        \__/
                    .'  O    \     /               /       \  "
                    (_____,    `._.'               |         }  \/~~~/
                    `----.          /       }     |        /    \__/
                            `-.      |       /      |       /      `. ,~~|
                                ~-.__|      /_ - ~ ^|      /- _      `..-'
                                    |     /        |     /     ~-.     `-. _  _  _
                                    |_____|        |_____|         ~ - . _ _ _ _ _>'''
    pass
