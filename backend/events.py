events = []


def add_event(message):

    events.insert(0, message)

    if len(events) > 20:
        events.pop()


def get_events():

    return events