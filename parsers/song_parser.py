import json

def parse_song(map_data):
    timestamps = []
    for timestamp, data in map_data.items():
        timestamps.append(int (timestamp))

    return timestamps

def get_obj_data(timpestamp, map_data):
    data = map_data[str (timpestamp)]
    print(data['name'])
    return data


if __name__ == "__main__":
    file = open("maps/red_light.json")
    map_data = json.load(file)
    timestamps = parse_song(map_data)
    data1 = get_obj_data(1, map_data)
    data2 = get_obj_data(30, map_data)

    print(timestamps)
    print(data1)
    print(data2)