from collections import defaultdict, OrderedDict

text = '''
"
The Korean Ministry of the Interior and Safety has raised crisis alerts to the 

highest level as Typhoon Khanun is heading north. The Central Disaster and 

Safety Countermeasures Headquarters has also increased its response level to 

Level 3 from Level 2.

According to forecasts by the Korea Meteorological Administration, Typhoon 

Khanun is expected to maintain its strength and arrive on the southern coast of 

the Korean Peninsula on Thursday morning before traversing the peninsula.

All regions across the country are expected to experience significant rainfall, 

with parts of Gangwon Province expecting over 600 millimeters (mm) and Gyeongsang 

Province over 300 mm.

The safety headquarters has urged related authorities to control basements, steep 

slopes, underground roads, riverbanks, coastal roads, and breakwaters, and to 

evacuate residents to minimize potential losses due to Typhoon Khanun.

The headquarters further stressed that areas affected by heavy rainfall should be 

swiftly restored, and popular locations such as beaches should be regulated to 

ensure the safety of visitors.

Residents in high-risk areas, such as mountainous regions and riverside 

communities, are advised to evacuate to shelters by Wednesday afternoon.

Additionally, there will be more allocations of public transportation services 

during commuting hours. In the event of emergencies, prompt disaster alerts will 

be disseminated to the public through text messages.

“We will make the best effort to prevent life loss by preemptively controlling 

risky areas and evacuating residents,” said Interior Minister Lee Sang-min.

He advised the public to monitor weather conditions and refrain from outdoor 

activities and unnecessary travel.
"
'''.lower().split()

word_count = defaultdict(lambda : 0)

for word in text:
    word_count[word] += 1

test_OrderedDict = OrderedDict(sorted(word_count.items(), key=lambda t:t[1], reverse=True)).items()

for i, v in test_OrderedDict:
    print(f"test_OrderedDict의 결과값 요소 : i : {i}, v : {v}")