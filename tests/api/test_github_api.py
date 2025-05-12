import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('Abrakadabraaaaaaaaaaaa')
    assert r['message'] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
#    print(r)
    assert r['total_count'] == 57
    assert 'become-qa-auto-aug2020' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('Abraakadabraaaaaaaaaa')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('A')
    assert r['total_count'] != 0

@pytest.mark.api
def test_emoji_is_received(github_api):
    r = github_api.get_emojis()
    assert r != {}
    #Перевіряю що словник не пустий
    assert '100' in r
    #Перевіряю що є смайл із неймом "100"
    assert r['100'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8'
    #Перевіряю що для смайла "100" правильна урла

@pytest.mark.api
def test_getting_commits(github_api):
    r = github_api.get_all_commits('RostyslavSeminka', 'AQA101_GlobalLogic')
    assert r != []
    #Перевіряю що у відповіді немає пустого списку
    assert 'SeminkaR' in r[0]['commit']['author']['name']
    #Перевіряю що автором останнього коміта є 'SeminkaR'

@pytest.mark.api
def test_getting_special_commit(github_api):
    r = github_api.get_special_commit('RostyslavSeminka', 'AQA101_GlobalLogic', '5b3599fa1328edd8a836523e7260cb5b553bfcb0')
    assert r != {}
    assert r['commit']['message'] == 'M17.Required_part'
    #Перевіряю що назва коміту "M17.Required_part"

@pytest.mark.api
def test_head_branches(github_api):
    r = github_api.get_head_branches('RostyslavSeminka', 'AQA101_GlobalLogic', '5b3599fa1328edd8a836523e7260cb5b553bfcb0')
    assert r != []
    assert r[0]['name'] == 'main'