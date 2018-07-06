from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    '''根据指定的国家，返回pygal使用的两个字母的国别码'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

if __name__ == '__main__':
    print(get_country_code("Andorra"))
    print(get_country_code("China"))
    print(get_country_code("United Arab Emirates"))
    print(get_country_code("Afghanistan"))
