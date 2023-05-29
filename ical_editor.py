from collections import defaultdict
from icalendar import Calendar, Event

def delete_duplicate_events(ics_file):
    # Read the .ics file
    with open(ics_file, 'rb') as file:
        cal = Calendar.from_ical(file.read())

    # Create a dictionary to store events by DESCRIPTION and date
    events_dict = defaultdict(list)

    # Iterate through all events in the calendar
    for component in cal.walk('VEVENT'):
        description = component.get('DESCRIPTION')
        start_date = component.get('DTSTART').dt.date()

        # Add the event to the dictionary using DESCRIPTION and date as the key
        events_dict[(description, start_date)].append(component)

    # Remove duplicate events
    for event_list in events_dict.values():
        if len(event_list) > 1:
            # Remove all but the first occurrence of the duplicate events
            for event in event_list[1:]:
                cal.subcomponents.remove(event)

    # Save the modified .ics file
    with open('modified.ics', 'wb') as file:
        file.write(cal.to_ical())

    print('Duplicate events have been removed. Modified .ics file saved as modified.ics')

# Provide the path to your .ics file
ics_file_path = 'Seances.ics'

delete_duplicate_events(ics_file_path)
