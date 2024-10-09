"""CSC108: Fall 2024 -- Assignment 1: Airline Tickets

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto Mississauga. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Rutwa Engineer, Dan Zingaro, Peter Dixon, Randy Hickey, Romina Piunno
"""

# Constants
YEAR = 0
MONTH = 4
DAY = 6
FROM = 8
TO = 11
SEAT = 14
FLYER = 17

WINDOW = 'window'
AISLE = 'aisle'
MIDDLE = 'middle'


def get_flyer_info(ticket: str) -> str:
    """Return the flyer number of the flyer for this ticket, if present. 
    Otherwise, return the empty string.

     >>> get_flyer_info('20230915YYZYEG12F')
     ''
     >>> get_flyer_info('20230915YYZYEG12F1236')
     '1236'
    """
    # Write the body of the function here
    return ticket[FLYER:]
# Write the rest of your Assignment 1 functions here


def visits_airport(ticket: str, airport: str) -> bool:
    """
    returns True if the given airport is either the from or to airport and false if otherwise
    >>> visits_airport('20230915YYZYEG12F','Yzz')
    False
    >>> visits_airport('20230915YYZYEG12F1236','YYZ')
    True
    """
    if airport in ticket:
        return True
    else:
        return False


def get_seat_type(ticket: str) -> str:
    """
    returns whether the seat is either a widnow, middle, or aisle
    >>> get_seat_type('20230915YYZYEG12F1236')
    'window'
    >>> get_seat_type('20230915YYZYEG12B1236')
    'middle'
    """
    if ticket[16:FLYER] == "A" or ticket[16:FLYER] == "F":
        return WINDOW
    elif ticket[16:FLYER] == "B" or ticket[16:FLYER] == "E":
        return MIDDLE
    elif ticket[16:FLYER] == "C" or ticket[16:FLYER] == "D":
        return AISLE
    else:
        return ''


def is_valid_seat(ticket: str) -> bool:
    """
    returns true if only the seat is a valid seat and returns false if otherwise
    >>> is_valid_seat('20230915YYZYEG25F1236')
    True
    >>> is_valid_seat('20230915YYZYEG30G1236')
    False
    """
    seat_no = int(ticket[SEAT:16])
    if 0 < seat_no <= 30 and ticket[16:FLYER] in ("A", "B", "C", "D", "E", "F"):
        return True
    else:
        return False


def is_valid_flyer(ticket: str) -> bool:
    """
    returns true if and only if the flyer number is a valid and returns false if otherwise
    >>> is_valid_flyer('20230915YYZYEG12F1236')
    True
    >>> is_valid_flyer('20230915YYZYEG12F123')
    False
    """
    if len(ticket[FLYER:]) == 4:
        if int(ticket[FLYER:18]) + int(ticket[18:19]) + int(ticket[19:20]) % 10 == int(ticket[20:]):
            return True
        else:
            return False
    elif len(ticket[FLYER:]) == 0:
        return True
    else:
        return False


def is_valid_ticket(ticket: str) -> bool:
    """
    Returns true if the ticket has a valid seat, valid flyer number, and different
    from and to airports.
    >>> is_valid_ticket('20230908YULYYZ07C2349')
    True
    >>> is_valid_ticket('20230908YYZYYZ07C2349')
    False
    """

    if ticket[FROM:TO] != ticket[TO:SEAT]:
        if is_valid_seat(ticket) and is_valid_flyer(ticket):
            return True
        else:
            return False
    else:
        return False


def days_until(ticket: str, date: str) -> int:
    """
    return the amount of days between the given date and ticket date
    >>> days_until('20230908YULYYZ07C2349','20230901')
    7
    >>> days_until('20230915YYZYEG12F1236','20240915')
    -365
    """

    date_year = int(date[:MONTH])
    date_month = int(date[MONTH:DAY])
    date_day = int(date[DAY:])
    ticket_year = int(ticket[YEAR:MONTH])
    ticket_month = int(ticket[MONTH:DAY])
    ticket_day = int(ticket[DAY:FROM])

    yrs_days = (ticket_year - date_year) * 365
    months_days = (ticket_month - date_month) * 30
    days = ticket_day - date_day
    return yrs_days + months_days + days
