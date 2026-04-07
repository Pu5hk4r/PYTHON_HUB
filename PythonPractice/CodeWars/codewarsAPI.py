# CodwarsAPI
# Get the list of integers for 'totalAuthored' and 'totalCompleted'
# of the nth ranker at Codewars Leaderboard.
# (1 <= n <= 500)
# See Example Test Cases for the expected data format.
#
# (Note 1 : Mind the title of this kata as well as https://dev.codewars.com/ )
#
# (Note 2 : It is recommended to finish Codewars Leaderboard before this kata. )
#
import json
from urllib.request import urlopen


def get_code_challenges(n):
    url = "https://www.codewars.com/api/v1/leaderboard/users"
    with urlopen(url) as response:
        data = json.loads(response.read())

    user = data['data'][n - 1]
    return [user['totalAuthored'], user['totalCompleted']]
