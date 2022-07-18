#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Sample data for Relationship Status below:
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


# In[14]:


'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if from_member in social_graph[to_member]["following"]:
        if to_member in social_graph[from_member]["following"]:
                return("friends")
        elif to_member not in social_graph[from_member]["following"]:
                return("follower")
    elif to_member in social_graph[from_member]["following"]:
        return("followed by")
    else: 
        return("no relationship")
    
relationship_status("@chums", "@jobenilagan", social_graph)


# In[2]:


'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]


# In[4]:


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    horizontal_list = []
    vertical_list = []
    a = len(board)

    # board for the vertical
    vertical_board = [x for x in zip(*board)]

    # set to check later on if there is a win
    for x in range(0,a):
        horizontal = set(board[x])
        horizontal_list.append(horizontal)

    for x in range(0,a):
        vertical = set(vertical_board[x])
        vertical_list.append(vertical)

    diagonal_updown = set([board[i][i] for i,v in enumerate(board)])
    diagonal_downup = set([board[a-1-i][i] for i,v in enumerate(board)])

    # checking the set if there is a winner 
    for y in range(0,len(horizontal_list)):
        len_horizontal = len(horizontal_list[y]) 

        if len_horizontal == 1:
            symbol = horizontal_list[y]
            winner = ', '.join(symbol)
            break
        else:
            for y in range(0,len(vertical_list)):
                len_vertical = len(vertical_list[y]) 

                if len_vertical == 1:
                    symbol = vertical_list[y]
                    winner = ', '.join(symbol)
                    break

                else:
                    if len(diagonal_updown) == 1:
                        symbol = diagonal_updown
                        winner = ', '.join(symbol)

                    elif len(diagonal_downup) == 1:
                        symbol = diagonal_downup
                        winner = ', '.join(symbol)

                    else:
                        winner = "NO WINNER"
    return winner

tic_tac_toe(board7)


# In[10]:


'''
Sample data for ETA below:
(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

# legs = {
#     ('a1', 'a2'): {
#         'travel_time_mins': 10
#     },
#     ('a2', 'b1'): {
#         'travel_time_mins': 10230
#     },
#     ('b1', 'a1'): {
#         'travel_time_mins': 1
#     }
# }


# In[11]:


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    current_location = first_stop
    total_time = 0
    
    while current_location != second_stop:

        for i in route_map:
            if current_location == i[0]:
                current_location = i[1]
                total_time += route_map[i]["travel_time_mins"]
                break
        
    return(total_time)
    
eta("upd", "dlsu", legs)


# In[ ]:




