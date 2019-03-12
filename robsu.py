import rg

class Robot:
    def act(self, game):
        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
        	if bot.player_id != self.player_id:
				if rg.dist(loc, self.location) <= 1:
        #            return ['attack', loc]
					print loc
					#print ("PlayerID: ", self.player_id)
					print ("RobotID: ", self.robot_id)

            
        # get enemies
        enemies = []
        for loc in around(self.location):
            if isenemy(loc):
                enemies.append(loc)

        moveable = []
        moveable_safe = []
        for loc in around(self.location):
            if isempty(loc):
                moveable.append(loc)
            if isempty(loc) and not isspawn(loc):
                moveable_safe.append(loc)
                

        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']
        
	def isenemy(l):
        if robots.get(l) != None:
            if robots[l]['player_id'] != self.player_id:
                return True
        return False           
