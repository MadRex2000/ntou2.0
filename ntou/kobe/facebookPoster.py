import facebook
graph = facebook.GraphAPI(access_token='token', version="3.0")


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
