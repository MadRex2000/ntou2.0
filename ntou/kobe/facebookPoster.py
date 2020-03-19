import facebook
graph = facebook.GraphAPI(access_token='EAAK9493PHmgBAPMOFMcGZAvzHnuBOxsjvDtbtkPPBrx7scDvAXPLMRh6sS5o1Fl7ickjiBKL1Hqjua0AnigybFWv0r3RqP4ZAvsKl7wq6wt9mYF1eisZC936gqSzraJ3k2lD1JPwGCpoQUC5TeEOm3zhKZCs3SPr9VyRuyzd4UlPhK7DVZCTR', version="3.0")


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
