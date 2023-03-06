# Properties

## Valid States

- Return 0 for non-created meeting (VS-1)
- Return > 0 if the meeting has been created (except for getnumOfParticipants) (VS-2)

## Variable transition

- Can only join meetings that have been started (VT-1)
- Can only end meetings that have been started and the endTime is greater than now
- Cancelling a meeting changes the meeting state to cancelled
- Ending a meeting changes the meeting state to ended
- Joining a meeting increases the number of participants

## High-level

- Can only schedule a meetingId that doesn't exist and is in the future (H-1)
- Can only cancel pending meetings
- Can only end started meetings
- Can join a meeting that has started

## Unit tests

- Can only start a meeting that is pending and within the start/end times (U-1)
- Can only cancel a meeting where the sender is the organizer and the meeting is pending

# Categorised

1. H-1 Otherwise will have conflicting meetings and corrupted state
2. H-2, H-3 and H-4;
