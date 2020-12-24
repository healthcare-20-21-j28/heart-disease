import json

with open('data/DiseaseData.json') as file:
    disease_data = json.load(file)


# for identify disease descripton and treatement
def disease_description(prob):
    if 10 > prob > 0:
        return disease_data['10']
    elif 20 > prob > 10:
        return disease_data['20']
    elif 30 > prob > 20:
        return disease_data['30']
    elif 40 > prob > 30:
        return disease_data['40']
    elif 50 > prob > 40:
        return disease_data['50']
    elif 60 > prob > 50:
        return disease_data['60']
    elif 70 > prob > 60:
        return disease_data['70']
    elif 80 > prob > 70:
        return disease_data['80']
    elif 90 > prob > 80:
        return disease_data['90']
    elif 110 > prob > 90:
        return disease_data['100']

