import random


def initialize_game():
    """Change this when you want to try out different variants of Blackjack!"""
    return BlackjackGame()
    # return AdvancedBlackjackGame()
    # return AlternativeDealerGame(14)
    # return AlternativeDealerGame(19)


class BlackjackGame:
    """A BlackjackGame implements a simplified version of blackjack.
    
    In a BlackjackGame:
    - aces always count as 1
    - the dealer's policy is to stand on 17
    - cards are drawn randomly with replacement from the deck
    """

    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        """Creates a standard deck of 52 cards.
        
        Returns
        -------
        list[int]
            a list of the 52 values of a standard deck of playing cards
            (face cards count as 10, aces count as 1)        
        """
        deck = [10] * 16
        for i in range(1, 10):
            deck += [i] * 4
        random.shuffle(deck)
        return deck

    def deal(self):
        """Deals two cards to the player and two cards to the dealer.
        
        Returns
        -------
        int, int
            the card total of the player, and the "up card" value of the dealer
        """
        player_card1 = self._draw_card()
        dealer_card1 = self._draw_card()
        player_card2 = self._draw_card()
        dealer_card2 = self._draw_card()
        self.player_cards = [player_card1, player_card2]
        self.dealer_cards = [dealer_card1, dealer_card2]
        return player_card1 + player_card2, dealer_card1

    def hit(self):
        """Deals another card to the player.
        
        Returns
        -------
        int
            the player's card total after the new card is dealt
        """
        self.player_cards.append(self._draw_card())
        return sum(self.player_cards)

    def _draw_card(self):
        """Draws a random card (with replacement) from the deck."""
        random.shuffle(self.deck)
        return self.deck[0]

    def stand(self):
        """Simulates the play of the dealer after the player stands.

        The dealer will HIT on a card total of 16 or less, and will STAND otherwise.

        Returns
        -------
        int
            the dealer's card total after the dealer stands or busts
        """
        total = sum(self.dealer_cards)
        while total <= 16:
            total += self._draw_card()
        return total


class DeterministicBlackjackGame(BlackjackGame):
    """A DeterministicBlackjackGame is a predictable blackjack game (for testing).
    
    Specifically, card values are always dealt according to the following sequence:
        10, 8, 6, 4, 2, 9, 7, 5, 3, 1
    
    In other words, the first card dealt always has a value of 10, the second card
    dealt always has a value of 8, etc. When the end of the sequence is reached,
    then we start over at the beginning.    
    """

    def __init__(self):
        super().__init__()
        self.next_card = 0

    def create_deck(self):
        """Creates a deck of 10 cards, for testing purposes."""
        return [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]

    def _draw_card(self):
        """Draws the next card from the deck."""
        card = self.deck[self.next_card]
        self.next_card += 1
        self.next_card = self.next_card % len(self.deck)
        return card
    

class AdvancedBlackjackGame(BlackjackGame):
    """An AdvancedBlackGame implements a more realistic version of blackjack.
    
    An AdvancedBlackjackGame differs from a BasicBlackjackGame in one respect:
    aces can count as 1 or 11. Effectively, an ace counts as 11 if the card total
    would not exceed 21. Otherwise, an ace counts as 1.
    """
    # TODO: complete this class (Question Three)


class AlternativeDealerGame(BlackjackGame):
    """An AlternativeDealerGame implements a different dealer strategy.
    
    The conventional dealer strategy is to stand whenever the dealer's card total
    is 17 or greater. In an AlternativeDealerGame(k), the dealer strategy is to
    stand whenever the dealer's card total is k or greater.
    """    
    # TODO: complete this class (Question Four)