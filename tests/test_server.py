import requests as req
from textwrap import dedent


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000')
    expected = dedent('''
        <html>
        <head>
            <title> cowsay </title>
        </head>
        <body>
            <header>
                <nav>
                <ul>
                    <li><a href="/cow">cowsay</a></li>
                </ul>
                </nav>
            <header>
            <main>
            </main>
        </body>
        </html>''')

    assert response.text == expected


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
    '''This function tests that a valid get requests sends back the talking dinosaur. Note: Had some difficulty testing the nicely formatted one since it had some single curly braces in it which threw off the f-string. Normal string didn't capture carriage returns properly.
    '''
    response = req.get('http://127.0.0.1:5000/cow?msg=hi')
    expected = b''' ____ \n< hi >\n ---- \n\\                             .       .\n \\                           / `.   .\' " \n  \\                  .---.  <    > <    >  .---.\n   \\                 |    \\  \\ - ~ ~ - /  /    |\n         _____          ..-~             ~-..-~\n        |     |   \\~~~\\.\'                    `./~~~/\n       ---------   \\__/                        \\__/\n      .\'  O    \\     /               /       \\  " \n     (_____,    `._.\'               |         }  \\/~~~/\n      `----.          /       }     |        /    \\__/\n            `-.      |       /      |       /      `. ,~~|\n                ~-.__|      /_ - ~ ^|      /- _      `..-\'   \n                     |     /        |     /     ~-.     `-. _  _  _\n                     |_____|        |_____|         ~ - . _ _ _ _ _>'''
    assert response.text.encode() == expected


def test_server_post_cow_returns_a_json_talking_steggy():
    '''This function tests that a valid post requests sends back a json object with a 'content' key and the byte-encoded cowpy image
    '''
    response = req.post('http://127.0.0.1:5000/cow?msg=hi')
    expected = {"content": " ____ \n< hi >\n ---- \n\\                             .       .\n \\                           / `.   .' \" \n  \\                  .---.  <    > <    >  .---.\n   \\                 |    \\  \\ - ~ ~ - /  /    |\n         _____          ..-~             ~-..-~\n        |     |   \\~~~\\.'                    `./~~~/\n       ---------   \\__/                        \\__/\n      .'  O    \\     /               /       \\  \" \n     (_____,    `._.'               |         }  \\/~~~/\n      `----.          /       }     |        /    \\__/\n            `-.      |       /      |       /      `. ,~~|\n                ~-.__|      /_ - ~ ^|      /- _      `..-'   \n                     |     /        |     /     ~-.     `-. _  _  _\n                     |_____|        |_____|         ~ - . _ _ _ _ _>"}
    assert response.json() == expected
