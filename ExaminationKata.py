import ExaminationKataConf
import random

class KataPicker:

    def __init__(self):
        # get kata configuration
        self.__confDefaults  = ExaminationKataConf.default
        self.__confExtras    = ExaminationKataConf.extras
        self.__confOrder     = ExaminationKataConf.order
    
    # get only basic kata for a given rank
    def __getConf(self, rank):
        rankIndx = self.__confOrder.index(rank)
        rankConf = self.__confDefaults[rankIndx]            
            
        return rankConf
        
    # get kata from previous ranks     
    def __getAllUniquePrevious(self, rank):
        previous = {}
                
        if (rank in self.__confOrder):    
            for i in range(0, self.__confOrder.index(rank)):      
                for kata in self.__confDefaults[i]['kata']:
                    previous[kata] = 1   

        return sorted(previous.keys())
        
    def getExamKata(self, rank):
        rand    = random.Random()
    
        examKata = {
            'normal'        : [],
            'varia'         : [],
            'previous'      : [],
            'extras'        : [],
            'extrasVaria'   : [],
        }
        
        conf = self.__getConf(rank)        
        
        count = 1
        # prepare normal kata
        if ('count' in conf):
            count = conf['count']
            
        for i in range(0, count):
            rand.shuffle(conf['kata'])
            examKata['normal'].append(conf['kata'][0])
        
        # prepare kata with variations
        rand.shuffle(conf['kata'])
        kata = conf['kata'][0]
        
        varia = self.__getRandom(self.__confExtras['varia'])
        examKata['varia'].append('%s - %s' % (kata, varia))
        
        # prepare previous kata
        prev = self.__getAllUniquePrevious(rank)
        rand.shuffle(prev)
        
        varia = self.__getRandom(self.__confExtras['varia'])
        examKata['previous'].append('%s - %s' % (prev[0] if len(prev) > 0 else '', varia))
        
        # prepare extras
        extra = self.__confExtras['no kata'] + self.__confExtras['dai ken'] + self.__confExtras['pinian']
        
        rand.shuffle(extra)
        examKata['extras'].append(extra[0])
        
        # prepare extras with variations
        rand.shuffle(extra)
        varia = self.__getRandom(self.__confExtras['varia'])
        examKata['extrasVaria'].append('%s - %s' % (extra[0], varia))
        
        return examKata
        
        
    def __getRandom(self, elems):
        rand    = random.Random()
        indx    = rand.randint(0, (len(elems)-1) )
        return  elems[indx]