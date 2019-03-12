import rg

class Robot:
    def act(self, game):
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        # move to un occupied spot
        locs = rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))
        
        if rg.toward(self.location, rg.CENTER_POINT) in locs:
    		return ['move', rg.toward(self.location, rg.CENTER_POINT)]    
    	else:
    		if len(locs)>=1:
    			return ['move', locs(0)] 
    		else:
    			return ['guard']    
            
        
