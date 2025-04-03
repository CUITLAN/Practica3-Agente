import random
from States.AgentConsts import AgentConsts

class GoalMonitor:

    GOAL_COMMAND_CENTRER = 0
    GOAL_LIFE = 1
    GOAL_PLAYER = 2
    def __init__(self, problem, goals):
        self.goals = goals
        self.problem = problem
        self.lastTime = -1
        self.recalculate = False

    def ForceToRecalculate(self):
        self.recalculate = True

    #determina si necesitamos replanificar
    def NeedReplaning(self, perception, map, agent):
        if self.recalculate:
            self.lastTime = perception[AgentConsts.TIME]
            return True
        if perception[AgentConsts.LIFE_X] != -1 and perception[AgentConsts.LIFE_Y] != -1 and perception[AgentConsts.HEALTH] < 3:
            self.recalculate = True
            return True
        if perception[AgentConsts.NEIGHBORHOOD_DOWN] == AgentConsts.PLAYER or perception[AgentConsts.NEIGHBORHOOD_DOWN] == AgentConsts.OTHER or perception[AgentConsts.NEIGHBORHOOD_DOWN] == AgentConsts.PLAYER or perception[AgentConsts.NEIGHBORHOOD_DOWN] == AgentConsts.OTHER or perception[AgentConsts.NEIGHBORHOOD_RIGHT] == AgentConsts.PLAYER or perception[AgentConsts.NEIGHBORHOOD_RIGHT] == AgentConsts.OTHER or perception[AgentConsts.NEIGHBORHOOD_LEFT] == AgentConsts.PLAYER or perception[AgentConsts.NEIGHBORHOOD_LEFT] == AgentConsts.OTHER:
            self.recalculate = True
            return True
        if perception[AgentConsts.NEIGHBORHOOD_DOWN] == AgentConsts.SHELL or perception[AgentConsts.NEIGHBORHOOD_UP] == AgentConsts.SHELL or perception[AgentConsts.NEIGHBORHOOD_LEFT] == AgentConsts.SHELL or perception[AgentConsts.NEIGHBORHOOD_RIGHT] == AgentConsts.SHELL:
            self.recalculate = True
            return True
        if AgentConsts.TIME - self.lastTime < 5:
            self.recalculate = True
            return True
        #Es necesario recalcular  siempre? 
        #TODO definir la estrategia de cuando queremos recalcular
        #puede ser , por ejemplo cada cierto tiempo o cuanod tenemos poca vida.
        #cada cierto tiempo, poca vida -> buscar vida, si jugador cera -> disparar jugador, si bala cerca -> esquivar, si nada de eso -> ir a command center
        return False
    
    #selecciona la meta mas adecuada al estado actual
    def SelectGoal(self, perception, map, agent):
        #TODO definir la estrategia del cambio de meta
        print("TODO aqui faltan cosas :)")
        return self.goals[random.randint(0,len(self.goals))]
    
    def UpdateGoals(self,goal, goalId):
        self.goals[goalId] = goal
