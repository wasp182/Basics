
res_data = [(0.1067122999811545, 0.1000802000053227, 0.0915308000985533), (0.17350619996432215, 0.16524859995115548, 0.22138979996088892), (0.31200410006567836, 0.23337420006282628, 0.40207930002361536), (0.4592543999897316, 0.398623300017789, 0.6054664000403136), (0.31572650000452995, 0.573522699996829, 0.5222339000320062), (0.5166024999925867, 0.4661561999237165, 0.5827985999640077), (0.5153662000084296, 0.8900303000118583, 0.7738196999998763), (0.7182540000649169, 1.0863664000062272, 0.7636502999812365), (1.0100255000870675, 0.9467926000943407, 0.857075700070709)]

def max_tuple(res)-> int:
     max1 = max(res)
     for index in range(len(res)):
         if max1 == res[index]:
             return index


freq=[]
for items in res_data:
    freq.append(max_tuple(items))

print(freq)

final = [[i for i in range(len(items)) if max(items) == items[i] ]for items in res_data]
print(final)