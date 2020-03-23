import facebook
graph = facebook.GraphAPI(access_token='EAAK9493PHmgBAJepxEyL9b04WNPGWOdQ2lhM1Abug2YqZBbz8Om908bxiQzRjcZA3ZBhbbZBb8iM9UbW5ZAJDm49Lar6gZCUK44hFc69RXxN3A94v4YyR6BwTCgPkVzzJqxlszcAAYB9CHT3P5smWPjXcy3qypZAmus16vWqZAhPcQZDZD', version="3.0")


class FbPoster():
    def __init__(self, id, post):
        self.id = id
        self.post = post

    def poster(self):
        return(graph.put_object(
          parent_object='100177881620069',
          connection_name="feed",
          message='#靠北海大二點零{} \n發文網址：http://www.rexwu.taipei \n{}'.format(self.id, self.post),
        ))
