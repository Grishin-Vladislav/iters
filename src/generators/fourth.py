def flat_generator2(list_of_lists):
    for pos, item in enumerate(list_of_lists):
        if type(item) is list:
            yield from flat_generator2(item)
        else:
            yield item
