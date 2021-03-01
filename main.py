import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://dc.urbanturf.com/pipeline"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
rows=[]
cols=['Title','Url','Image url', 'Location', 'Project type', 'Status', 'Size']
for data in soup.find_all('div',attrs={'class':'pipeline-item'}):
    title=data.a['title']
    url=data.a['href']
    image = data.a.img['src']
    for ele in data.find_all('p'):
        if not ele.h2:
            if ele.span.text=="Location:":
                ele.span.extract()
                location = ele.text.strip()
            elif ele.span.text=="Project type:":
                ele.span.extract()
                pro_type = ele.text.strip()
            elif ele.span.text=="Status:":
                ele.span.extract()
                status = ele.text.strip()
            elif ele.span.text=="Size:":
                ele.span.extract()
                size = ele.text.strip()
    rows.append([title, url, image, location, pro_type, status, size])
df=pd.DataFrame(rows, columns=cols)
df.to_excel('DC pipeline.xlsx', index=False)

