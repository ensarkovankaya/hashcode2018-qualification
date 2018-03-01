class Ride:

    def __init__(self, id, **kwargs):
        self.id = int(id)
        self.start_row = int(kwargs.get('start_row'))
        self.start_column = int(kwargs.get('start_column'))
        self.finish_row = int(kwargs.get('finish_row'))
        self.finish_column = int(kwargs.get('finish_column'))
        self.earliest_start = int(kwargs.get('earliest_start'))
        self.latest_finish = int(kwargs.get('latest_finish'))
        self.is_taken = False

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<Ride %s>' % self.id
