texts = ['他媽的','他媽','幹你娘','雞巴毛','廢物', '靠北']
nonTexts = ['靠北海大']

class checkPost():
    def __init__(self):
        pass
    def check(post):
        for j in nonTexts:
            for i in texts:
                if i in post and j not in post:
                    return False
        return True
