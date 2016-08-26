
self.northeast = ('New York','Pennsylvania','New Jersey','Connecticut','Rhode Island','Massachusetts','New Hampshire','Vermont','Maine')
self.southeast = ('Arkansas','Louisiana','Mississippi','Alabama','Tennessee','Kentucky','Georgia','North Carolina','South Carolina','Virginia','West Virginia','Maryland','Delaware','Washington DC', 'Florida')
self.midwest = ('North Dakota','South Dakota','Nebraska','Kansas','Minnesota','Iowa','Missouri','Wisconsin','Illinois','Michigan','Ohio','Indiana')
self.west = ('Montana','Idaho','Wyoming','Colorado','Utah','Oregon','Washington', 'California','Nevada')
self.southwest = ('Texas','Arizona','New Mexico','Oklahoma')
self.other = ('Unspecified','Puerto Rico','Hawaii','Alaska')

def _to_region(self,state):    
    if state in self.northeast:
        return 0
    elif state in self.southeast:
        return 1
    elif state in self.midwest:
        return 2
    elif state in self.west:
        return 3
    elif state in self.southwest:
        return 4
    else:
        return 5
def add_region(self):
    self.df['region'] = self.df_in['state'].apply(_to_region)