def parse(file):
    print("Opening file: %s" % file)

    data = {}

    with open(file, 'r') as input_file:
        rows, columns, vehicles, number_of_rides, bonus, total_steps = input_file.readline().strip().split()
        data['rows'] = int(rows)
        data['columns'] = int(columns)
        data['vehicles'] = int(vehicles)
        data['number_of_rides'] = int(number_of_rides)
        data['bonus'] = int(bonus)
        data['total_steps'] = int(total_steps)
        data['rides'] = {}

        for ride_id in range(int(number_of_rides)):
            start_row, start_column, finish_row, finish_column, earliest_start, latest_finish = input_file.readline().strip().split()
            data['rides'][ride_id] = {
                'start_row': int(start_row),
                'start_column': int(start_column),
                'finish_row': int(finish_row),
                'finish_column': int(finish_column),
                'earliest_start': int(earliest_start),
                'latest_finish': int(latest_finish)
            }

    return data
