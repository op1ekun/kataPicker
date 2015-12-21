# it was easier to hardcode it as python module than to write some fancy config file

default = (
    {   'kata'  : ['taikyoku shodan', 'taikyoku nidan', 'taikyoku sandan'] },
    {   'kata'  : ['heian shodan'] },
    {   'kata'  : ['heian nidan']  },
    {   'kata'  : ['heian sandan'] },
    {   'kata'  : ['heian yodan']  },
    {   'kata'  : ['heian godan']  },
    {   'kata'  : ['tekki shodan'] },
    {   'kata'  : ['bassai dai']   },
    {   'kata'  : ['empi', 'jion', 'hangetsu', 'kanku dai'] },
    {   'kata'  : ['empi', 'jion', 'hangetsu', 'kanku dai'] },
    {   
        'kata'  : ['empi', 'jion', 'hangetsu', 'kanku dai', 'bassai dai'],
        'count' : 3 
    },
    {
        'kata'  : ['empi', 'jion', 'hangetsu', 'kanku dai', 'bassai dai'],
        'more'  : ['bassai sho', 'kanku sho' , 'jitte', 'sochin', 'gankaku', 'nijushiho', 'meikyo', 'chinte']
    },
    {
        'kata'  : ['bassai sho', 'kanku sho' , 'jitte', 'sochin', 'gankaku'],
        'more'  : ['nijushiho', 'meikyo', 'gojushiho', 'unsu']    
    },
    {   'kata'  : ['nijushiho', 'gojushiho', 'unsu'] },
)

ranks = ['9kyu', '8kyu', '7kyu', '6kyu', '5kyu', '4kyu', '3kyu', '2kyu', '1kyu', '1dan', '2dan', '3dan', '4dan', '5dan']

extras = {
    'no kata' : ['mawari no kata', 'gyaku zuki no kata', 'kokutsu dachi no kata', 'zenkutsu dachi no kata'],
    'dai ken' : ['dai itsu ken', 'dai ni ken', 'dai san ken', 'dai yon ken'],
    'pinian'  : ['pinian shodan', 'pinian nidan', 'pinian sandan', 'pinian yodan', 'pinian godan'],
    'varia'   : ['ura kata', 'from the first to the last technique', 'with rotations', 'attack forwards/block backwards', 'all techniques backwards'],
}