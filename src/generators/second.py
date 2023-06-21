def flat_generator1(list_of_lists):
    for item in list_of_lists:
        if type(item) is list:
            yield from flat_generator1(item)
        else:
            yield item
