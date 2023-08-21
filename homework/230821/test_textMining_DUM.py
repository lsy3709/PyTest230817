from collections import defaultdict, OrderedDict
from collections import Counter

text = '''
"The sunset's longer
Where I am from
Where dreams go to die
While having fun
The boys fix their cars and
Girls heat it up
Love is so good when
The love is young
Yeah, there's so much history in these streets
And mama's good eats
And wonder on repeat
There's soo much history in my head
The people I've left
The ones that I've kept
Have you heard me on the radio, did you turn it up?
On your blown-out stereo in suburbia?
Could be playing hide and seek from home
Can't replace my blood
Yeah, it seems I'm never letting go
Of suburbia
Swallow nostalgia, chase it with lime
Better than dwelling
And chasing time
Missing occasions
I can't rewind
Can't help but feel like I've lost what's mine
Yeah, there's so much history in these streets
And mama's good eats
And wonder on repeat
There's soo much history in my head
The people I've left
The ones that I've kept
Have you heard me on the radio, did you turn it up?
On your blown-out stereo in suburbia?
Could be playing hide and seek from home
Can't replace my blood
Yeah, it seems I'm never letting go
Of suburbia
Yeah, they're all the same but nothing ever changes
Through the new lines that are on their faces
Yeah, they're all the same that nothing ever changes
Through the new lines that are on their faces oh
There's so much history in these streets
And mama's good eats
And wonder on repeat
There's soo much history in my head
The people I've left
The ones that I've kept
Have you heard me on the radio, did you turn it up?
On your blown-out stereo in suburbia?
Could be playing hide and seek from home
Can't replace my blood
Yeah, it seems I'm never letting go
Of suburbia, oh oh oh oh"
'''.lower().split()

print(f"가장 많이 쓴 단어 10가지 : {Counter(text).most_common(10)}")
