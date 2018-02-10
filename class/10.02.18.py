import collections

with open('all-seasons.csv', encoding='utf-8') as f:
#    text = f.read()
#print(text[:100])
    quote = ''
    d = {}
    for line in f:
        if line == 'Season,Episode,Character,Line\n':
            continue
        if quote == '':
            season, episode, char, quote = line.split(',', maxsplit=3)
            quote = quote.strip()
        else:
            quote += line
        if line == '"\n':
            #if season in d:
            #    d[season].append(quote)
            #else:
            #    d[season] = [quote]
            season_dict = d.setdefault(season, {})
            episode_dict = season_dict.setdefault(episode, {})
            quote_list = episode_dict.setdefault(char, [])
            quote_list.append(quote.strip())
            quote = ''  
print(d['9']['4']['Kenny'])

c = collections.Counter()
for k, v in d.items():
    c[k] = len(v)
print(c.most_common(5))

cc = collections.Counter()
season = '10'
episode = '5'
for k, v in d[season][episode].items():
    cc[k] = len(v)
print(cc.most_common())






#print(season, episode, char, quote)
           
            #print(season, episode, char, quote)
            #break
        #print(season, episode, char, quote)
        #break

