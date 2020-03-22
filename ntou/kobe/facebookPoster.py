import facebook
graph = facebook.GraphAPI(access_token='token', version="3.0")


class FbPoster():
    def __init__(self):
        pass

    def poster(self, id, post):
        return(graph.put_object(
          parent_object='100177881620069',
          connection_name="feed",
          message='#靠北海大二點零{} \n發文網址：http://www.rexwu.taipei \n{}'.format(id, post),
        ))

    def imgPoster(self, id, post, img):
        return(graph.put_object(
          parent_object='100177881620069',
          connection_name="feed",
          message='#靠北海大二點零{} \n發文網址：http://www.rexwu.taipei \n{}'.format(id, post),
        ))
