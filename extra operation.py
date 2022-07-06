#remove duplicates
list1 = []
def distinct(scene):
  for order in range(0,20):
    list1 = summary.loc[geo[order],scene]
    summary.loc[geo[order],scene] = list(set(list1))

for scene in senarios:
  distinct(scene)

#summary by rows
summary['summary'] = summary['summary'].astype('object')#不然没法赋值

def concatenate(place):
  words_row = []
  for scene in senarios:
    list_ = summary.loc[place,scene]
    words_row.extend(list_)
  summary.at[place,'summary'] = words_row

for place in geo:
  concatenate(place)


#delete '的' in the string
def del_de(block):
  for i in range(len(block)):
    if block[i][-1] == '的':
      block[i] = block[i][:-1]

for num in range(20):
  del_de(summary['summary'].iloc[num])


from collections import Counter
# order by frequency of occurence
def count_word(block):
  d2 = Counter(block)
  sorted_x = sorted(d2.items(), key=lambda x: x[1], reverse=True)
  return sorted_x


#fill in the block of form
summary['high_frequency'] = summary['high_frequency'].astype('object')
for i in range(20):
  selected = count_word(summary['summary'].iloc[i])[:10]
  summary.at[geo[i],'high_frequency'] = selected