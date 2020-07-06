import pprint

message = ''' I wish I never went to MIT. I could have gone to a state school, finished early because my AP credits would have counted for something, and I would have left with my self confidence and mental health in tact. Instead, I chose to go to MIT because it was my "dream school", and I now have crippling depression and anxiety, wasted an extra year here because the mental health problems made it really hard to concentrate on my work, and for what? A fancy name on my resume? I've yet to find a job because nobody cares what school you went to if you don't know React or Node or TF or whatever. Apparently the MIT network doesn't mean anything because I've been directly rejected by several MIT alumni. And I can't go to grad school because my grades are shit, and I'm burnt out anyways. The only redeeming thing I got was the friends I met here, but like who knows what cool people I could have met at another school? So yeah, 1/10 would not recommend.'''

count = { }

for character in message.upper():
        count.setdefault (character, 0)
        count[character] = count[character] + 1

pprint.pprint(count)

cctext = pprint.pformat(count)
print(cctext)
