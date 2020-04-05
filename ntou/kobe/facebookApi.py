import facebook, configparser, os

config = configparser.ConfigParser()
config.read('kobe/config.ini')
#token = str(config['FB']['Token'])

graph = facebook.GraphAPI(access_token = config['fb']['token'], version = "3.0")

class FbManger():
    def __init__(self, id, post, time):
        self.id = id
        self.post = post
        self.time = time

    def poster(self):
        return graph.put_object(
            parent_object='100177881620069',
            connection_name="feed",
            message='#靠北海大二點零{}\n發文網址：https://www.kobentou.site\n{}\n發文時間：{}'.format(self.id, self.post, str(self.time)[:16]),
            )['id']

    def imgPoster(self, img):
        return graph.put_photo(
            parent_object='100177881620069',
            image=open(os.path.join('media', str(img)), 'rb'),
            message='#靠北海大二點零{}\n發文網址：https://www.kobentou.site\n{}\n發文時間：{}'.format(self.id, self.post, str(self.time)[:16]),
            )['post_id']

    def postDeleter(self, token):
        return(graph.delete_object(id = token))
