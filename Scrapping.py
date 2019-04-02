#!C:\Users\Bhavya Mulpuri\AppData\Local\Programs\Python\Python36-32\python.exe
import requests
from bs4 import BeautifulSoup
import cgi, cgitb
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("Content-Type:text/html\r\n\r\n")
cgitb.enable();
form = cgi.FieldStorage();

state = "S29";""" form["s1"].value"""
constituency =  "82" ;"""form["s2"].value"""


url = "http://eciresults.nic.in/Constituencywise" + state + constituency + ".htm?ac=" + constituency;
print(url);

page = requests.get(url);
soup = BeautifulSoup(page.content, 'html.parser');
table = soup.find('table', border="1");
t_rows = table.find_all('tr', style="font-size:12px;");


result = [];

with open('data.csv', 'w') as f:
    for row in t_rows:
        result = row.find_all('td');
        # print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));
        data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
        data_writer.writerow(
            ['%s' % (result[0].text.strip()), '%s' % (result[1].text.strip()), '%s' % (result[2].text.strip())]);
        
var = [];
x_axis = [];
y_axis = [];
z_axis = [];

with open('data.csv', 'r') as f:
    var = csv.reader(f, delimiter=",");
    for i in var:
        if len(i) is not 0:
            x_axis.append(i[0]);
            y_axis.append(i[1]);
            z_axis.append(int(i[2]));

fig = plt.figure()
plt.bar(x_axis, z_axis, width=0.8, color=['red', 'green', 'pink', 'blue', 'black'])
for i,v in enumerate(z_axis):
    plt.text(x_axis[i] ,v ,str(v),horizontalalignment = 'center',fontsize =10);
plt.xlabel('candidates');
plt.ylabel('number of votes');
plt.title('Constituencywise result Data Visualization');
num=np.arange(len(x_axis));
plt.xticks(num,x_axis,fontsize=6,rotation=30);
plt.show();
plt.savefig('C:/xampp/htdocs/plot.pdf');

