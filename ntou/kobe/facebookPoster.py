import facebook
graph = facebook.GraphAPI(access_token='EAAK9493PHmgBAEky4Hc4ZBr5ghCcYljA47m0fZBoZAYrrAsgzxNHJbZA6OWU6Htk5NJS99vpq9pEkFWHIqaI3EK5v8c4ZAWuASGTjJfcMzYiskZBEZCFO7QtOAznfk1JJeWqHfxMtWKlTGHku6lAhHFPlqjcDbJYxxa7ozE8kklTU17GZBmsDAmtBzw3KUCB3tZB8PgJLWhqUZCQZDZD', version="3.0")


class FbPoster():
    def __init__(self):
        pass

    def poster(id, post):
        return(graph.put_object(
          parent_object='100177881620069',
          connection_name="feed",
          message='#靠北海大二點零{} \n發文網址：http://www.rexwu.taipei \n{}'.format(id, post),
        ))

    def imgPoster(id, post, img):
        return(graph.put_object(
          parent_object='100177881620069',
          connection_name="feed",
          message='#靠北海大二點零{} \n發文網址：http://www.rexwu.taipei \n{}'.format(id, post),
        ))
