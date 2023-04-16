from environment import Environment

class BlackjackEnvironment(Environment):
    """A BlackjackEnvironment simulates being at a blackjack table.
    
    The initial state is called 'START'. It has only possible action: 'deal'.
    If you do the action 'deal' in state 'START', then it will bring you to state
    (player_total, up_card), a tuple of two integers where:
    - player_total is the total of the first two cards dealt to the player
    - up_card is the value of the dealer's face up card

    States of the form (player_total, up_card) have two possible actions: 'hit' 
    and 'stand'.

    The final states are 'WIN', 'LOSE', and 'DRAW'. Final states have no possible
    actions. You reach a final state by going bust (i.e. the player's card total
    goes over 21), or by taking the action 'stand' in any (player_total, up_card)
    state.

    The reward for being in state 'WIN' is 1. The reward for being in state 'LOSE'
    is -1. The reward for any other state is 0.

    Transitioning from one state to another should be determined by the
    provided BlackjackGame. Specifically:
    - .do_action("deal") should update the state based on the game state of the
      BlackjackGame after calling the .deal method.
    - .do_action("hit") should update the state based on the game state of the
      BlackjackGame after calling the .hit method.
    - .do_action("stand") should update the state based on the game state of the
      BlackjackGame after calling the .stand method.
    """

    # TODO: complete this class (Question Two)