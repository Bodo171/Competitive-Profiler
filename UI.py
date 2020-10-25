from settings import Settings


def get_color(rating):
    color = '#D3D3D3' #light gray
    font = ''
    #if rating == 'Inactive':
    #    font = 'font-weight: italic'
    if isinstance(rating, int) or isinstance(rating, float):
        for i in range(len(Settings.colors)):
            if rating > Settings.colors[i][0]:
                color = Settings.colors[i][1]
        font = 'font-weight: bold'
    return 'color: ' + color + ';' + font


def get_tag(tag):
    return Settings.tags.get(tag, 'is-light')
