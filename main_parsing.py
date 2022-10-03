import requests
from bs4 import BeautifulSoup


def text_change(text):
    return text.replace("\n", "").replace(" ", "")


league_id = {'EPL': 'tournament-5c9dfa8099bab85b0d347cbc',
             'La_liga': 'tournament-5c9dfa7e99bab859223e8026',
             'Seria_A': 'tournament-5c9dfa8299bab8590b159196',
             'Bundes_Liga': 'tournament-5c9dfa8599bab859223e8042',
             'League_One': 'tournament-5c9dfa8499bab85b4c2b539c'
             }

league_country = {'EPL': 'ENG',
                  'La_liga': 'ESP',
                  'Seria_A': 'ITA',
                  'Bundes_Liga': 'DEU',
                  'League_One': 'FRA'
                  }


def parsing(ID, country, url):
    headers = {
        'accept':
            'text/html,application/xhtml+xml,'
            'application/xml;q=0.9,image/avif,'
            'image/webp,image/apng,*/*;q=0.8,'
            'application/signed-exchange;v=b3;q=0.9',
        'user-agent':
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/104.0.0.0 Safari/537.36'
    }
    games = ''
    response_for_parsing = requests.get(url, headers=headers)
    if response_for_parsing.status_code != 200:
        return 'Сайт не отвечает, попробуйте позднее'
    soup = BeautifulSoup(response_for_parsing.text, 'html.parser')
    championship_country = \
        soup.find('div', class_='tournaments-item category-' + country)
    if championship_country is None:
        return 'Матчей в этот день не найдено'
    championship_id = \
        championship_country.find('div', class_='tournaments-title', id=ID)
    if championship_id is None:
        return 'Матчей в этот день не найдено'
    all_games = championship_country. \
        find_all('div', class_='tournaments-match tournaments-game-item')

    for game in all_games:
        step_one = game.find('div', class_='teams')
        step_two = step_one.find('div', class_='team-info teamHost')
        team_home = step_two.find('span', class_='name ellipsis').text

        step1 = game.find('div', class_='teams')
        step2 = step1.find('div', class_='team-info teamGuest')
        team_guest = step2.find('span', class_='name ellipsis').text

        time_on_site = game.find('span', class_='data') \
            .find('span', class_='font-1rem').text
        time = text_change(time_on_site)

        game_status_on_site = game.find('span', class_='status finished')

        game_minute = game. \
            find('span',
                 class_='matchMinute matchState matchStatus matchLive')
        if game_status_on_site is None:
            if game_minute is None:
                games = games + f'Время начала матча: {time}' + \
                        '\n' + f'{team_home} VS {team_guest}' + \
                        '\n' + ' ' + '\n'
            else:
                score_home_on_site = game.find('div', class_='main-score'). \
                    find('span', class_='point scoreHost').text
                score_home = text_change(score_home_on_site)
                score_guest_on_site = game.find('div', class_='main-score'). \
                    find('span', class_='point scoreGuest').text
                score_guest = text_change(score_guest_on_site)
                games = games + \
                    f'Время начала матча: {time}' \
                    + '\n' + f'Минута: {game_minute.text}' \
                    + '\n' + f'{team_home} {score_home} : {score_guest} ' \
                    f'{team_guest}' + '\n' + ' ' + '\n'

        else:
            game_status = text_change(game_status_on_site.text)
            score_home_on_site = game.find('div', class_='main-score'). \
                find('span', class_='point scoreHost').text
            score_home = text_change(score_home_on_site)
            score_guest_on_site = game.find('div', class_='main-score'). \
                find('span', class_='point scoreGuest').text
            score_guest = text_change(score_guest_on_site)
            if game_status == 'Завершен':
                games = games + \
                        f'Время начала матча: {time}' + '\n' \
                        + f'{team_home} {score_home}:{score_guest} {team_guest}' \
                        + '\n' + game_status + '\n' + ' ' + '\n'
            else:
                games = games + \
                        f'Время начала матча: {time}' + '\n' \
                        + f'{team_home} VS {team_guest}' + '\n' \
                        + game_status + '\n' + ' ' + '\n'
    return games
