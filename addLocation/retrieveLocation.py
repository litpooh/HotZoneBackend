import requests
import json
from .models import Location
# /param keyword location search string to GeoDate Store
# search location from GeoData Store
# Compare the result with hotzone location database by name, xcoord and ycoord
# \return back the location json with existing location on the top of the list
def searchAndCompareLocation(keyword):
    # keyword = "HKU"
    r = requests.get(f"https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q={keyword}")
    # if the request is ok
    if r.status_code == requests.codes.ok:
        existingLocation = []
        locationsJson = json.loads(r.text)
        # find out existing location in the returned data
        for i, location in enumerate(locationsJson):
            # return match location with name, x and y
            querySet = Location.objects.filter(name=location['nameEN'],xcoord=location['x'],ycoord=location['y'])
            # if larger than 0, then the location exist in the database
            if len(querySet) > 0:
                print(querySet)
                # pop out the location and add the existingLocation array for later add back
                existingLocation.append(locationsJson.pop(i))

        # add back the existing location on the top
        for l in existingLocation:
            locationsJson.insert(0,l)
        
        return locationsJson
    else:
        return -1


if __name__ == "__main__":
    l = searchAndCompareLocation("HKU")
    print(l)