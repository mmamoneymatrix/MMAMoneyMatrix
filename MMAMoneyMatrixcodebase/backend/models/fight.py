class Fight:
    def __init__(self, data):
        self.id = data.get('id')
        self.fighter_a_id = data.get('fighter_a_id')
        self.fighter_b_id = data.get('fighter_b_id')
        self.winner_id = data.get('winner_id')
        self.method = data.get('method')
        self.round = data.get('round')
        self.time = data.get('time')
        self.event = data.get('event')
        self.date = data.get('date')
        
    def to_dict(self):
        return self.__dict__
