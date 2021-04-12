from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
def school_look_up(request):

    listForSchool = []
    if request.method =='POST':
        try:

            q = request.POST['zipCode']


            url = 'https://gs-api.greatschools.org/schools?zip=' + q + '&limit=5'
            headers = {

                'x-api-key': 'K6DrqSDyBy2ALQ3Ozih9ia4narAtJKGq8WGaJf6J',

            }
            response = requests.request("GET", url, headers=headers)
            results = response.json()
            name = []
            school_summary = []
            type = []
            level = []
            street = []
            city = []
            state = []
            zipcode = []
            phone = []
            county = []
            overview_url = []
            rating = []
            for result in range(len(results['schools'])):
                name.append(results['schools'][result]['name'])
                school_summary.append(results['schools'][result]['school-summary'])
                type.append(results['schools'][result]['type'])
                level.append(results['schools'][result]['level'])
                street.append(results['schools'][result]['street'])
                city.append(results['schools'][result]['city'])
                state.append(results['schools'][result]['state'])
                zipcode.append(results['schools'][result]['zip'])
                phone.append(results['schools'][result]['phone'])
                county.append(results['schools'][result]['county'])
                overview_url.append(results['schools'][result]['overview-url'])
                rating.append(results['schools'][result]['rating'])

            schoollist = zip(name, school_summary, type, level, street, city, state, state, zipcode, phone, county,
                             overview_url, rating)
            context = {

                'schoolInfo': schoollist

            }
            return render(request, 'school/index.html', context)

        except:
            return HttpResponse("Enter valid zip code ")
    return render(request,'school/index.html')





