class Fighter:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.height = data.get('height')
        self.reach = data.get('reach')
        self.slpm = data.get('slpm')
        self.striking_accuracy = data.get('striking_accuracy')
        self.sapm = data.get('sapm')
        self.striking_defense = data.get('striking_defense')
        self.td_avg = data.get('td_avg')
        self.td_acc = data.get('td_acc')
        self.td_def = data.get('td_def')
        self.sub_avg = data.get('sub_avg')
        self.gym_tier = data.get('gym_tier', 'C')
        self.underdog_level = data.get('underdog_level', 'none')
        
        # Derived Metrics
        self.strike_diff = self.slpm - self.sapm
        self.cardio_index = data.get('cardio_index', 50)
        self.damage_tolerance = data.get('damage_tolerance', 50)

    def to_dict(self):
        return self.__dict__
