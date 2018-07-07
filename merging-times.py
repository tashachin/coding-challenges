def merge_ranges(meetings):
    """Takes a list of meeting times from different teams and returns a condensed list based on time blocks.

    >>> [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    [(0, 1), (3, 8), (9, 12)]
    """

    # earlier start_time = first meeting

    # don't assume meeting times are given in order
    # meeting times are stored as tuples representing 30min blocks

    # if first tuples end time is greater than second tuples start time
    # replace end time of meeting with second tuples endtime (if greater)

    # Sort by meeting start times
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    # if the current meeting overlaps with the last merged meeting,
    # replace the merged meeting's end time with the later of the two
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings