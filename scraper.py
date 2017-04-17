import scraperwiki
from pyquery import PyQuery

url = 'https://www.vrbo.com/vacation-rentals?swLat=41.02271946788004&swLong=-124.16536826990239&neLat=41.108011129393624&neLong=-124.0891506185352&zoom=13&page=1&region=2179&searchTermContext=b1134c31-65a3-4128-bb00-74656f864008'

q = PyQuery(url)

print q('.ratesdetails').text()


