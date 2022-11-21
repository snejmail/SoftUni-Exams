def start_spring(**kwargs):
    spring_objects = {}
    for name, type in kwargs.items():
        if type in spring_objects:
            spring_objects[type].append(name)
        else:
            spring_objects[type] = [name]

    sorted_spring_objects = sorted(spring_objects.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for object_type, object_name in sorted_spring_objects:
        result += object_type + ":\n-"
        sorted_names = sorted(object_name)
        result += '\n-'.join([n for n in sorted_names]) + '\n'


    return result

