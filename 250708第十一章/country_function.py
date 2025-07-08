def country(city_name,country_name,population=0):
    if population:
        string=f"{city_name},{country_name}-population {population}"
    else:
        string=f"{city_name},{country_name}"
    return string.title()