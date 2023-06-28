import datetime

def numbers_format(value):
    """Makes a good looking numbers format."""

    return '{:,}'.format(value).replace(',', ' ')


def format_info(info, application_type):
    """Formats info from database to fill google sheets."""

    info = list(info[1::])

    for num, field in enumerate(info):
        if field is None:
            info[num] = '-'
    
    if info[-3] != '-':
        info[-3] = datetime.datetime.strftime(info[-3], '%d.%m.%Y')
    else:
        info[-3] = datetime.date.strftime((datetime.datetime.utcnow() + datetime.timedelta(hours=3)), '%d.%m.%Y')

    if application_type == 'telegram':
        if info[11] != '-':
            if info[11] == 1:
                info[11] = 'да'
            else:
                info[11] = 'нет'

        if info[12] != '-':
            if info[12] == 1:
                info[12] = 'да'
            else:
                info[12] = 'нет'

    elif application_type == 'mobile':
        info.pop(10)

        if info[11] != '-':
            if info[11] == 1:
                info[11] = 'да'
            else:
                info[11] = 'нет'

        info.pop(12)

    elif application_type == 'web':
        if info[10] != '-':
            if info[10] == 1:
                info[10] = 'да'
            else:
                info[10] = 'нет'

        if info[11] != '-':
            if info[11] == 1:
                info[11] = 'да'
            else:
                info[11] = 'нет'

        if info[12] != '-':
            if info[12] == 1:
                info[12] = 'да'
            else:
                info[12] = 'нет'

    info = info[:-2]
    return info