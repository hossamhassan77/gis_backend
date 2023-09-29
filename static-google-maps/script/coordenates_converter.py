def coordsList_to_dict_of_coords(coord_list: list) -> list:
    coord_dict = {}
    list_of_dicts = []
    list_of_dicts = []
    for i in coord_list:
        coord_dict["lat"] = i[1]
        coord_dict["lng"] = i[0]
        list_of_dicts.append(coord_dict)
        coord_dict = {}
    print(list_of_dicts)

coordsList_to_dict_of_coords( [
            [
              -122.03851614290173,
              37.563617841353405
            ],
            [
              -122.03364971993358,
              37.5584743289231
            ],
            [
              -122.02699334828768,
              37.561238271982575
            ],
            [
              -122.03667398541054,
              37.56546922019159
            ],
            [
              -122.03851614290173,
              37.563617841353405
            ]
          ])