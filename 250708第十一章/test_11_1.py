from country_function import country
def test_city_country():
    test_name=country('santiago','chile')
    assert test_name == 'Santiago,Chile'

def test_city_country_population():
    test_name=country('san','chi',50)
    assert test_name == 'San,Chi-Population 50'