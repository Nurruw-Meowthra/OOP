"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards = []

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        if len(self.cards) >= 5:
            return False
        if card.value not in self.values or card.suit not in self.suits:
            return False
        for c in self.cards:
            if c.value == card.value and c.suit == card.suit:
                return False
        return True

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card):
            self.cards.append(card)

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        for c in self.cards:
            if c.value == card.value and c.suit == card.suit:
                return True
        return False

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.cards

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        for card in self.cards:
            if card.value not in self.values:
                return False
        sorted_cards = sorted(self.cards, key=lambda c: self.values.index(c.value))
        for i in range(1, len(sorted_cards)):
            if self.values.index(sorted_cards[i].value) - self.values.index(sorted_cards[i - 1].value) != 1:
                return False
        return True

    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        if len(self.cards) == 0:
            return False
        suit = self.cards[0].suit
        for card in self.cards:
            if card.suit != suit:
                return False
        return True

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        for card in self.cards:
            if card.value not in self.values:
                return False
        value_counts = {}
        for card in self.cards:
            if card.value not in value_counts:
                value_counts[card.value] = 0
            value_counts[card.value] += 1
        has_three_of_a_kind = False
        has_pair = False
        for count in value_counts.values():
            if count == 3:
                has_three_of_a_kind = True
            elif count == 2:
                has_pair = True
        return has_three_of_a_kind and has_pair

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        cards = self.cards
        for card in cards:
            if card.value not in self.values:
                return False
        counter = {}
        for card in cards:
            if card.value not in counter:
                counter[card.value] = 0
            counter[card.value] += 1
        if 4 in counter.values():
            return True
        return False

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        cards = self.cards
        for card in cards:
            if card.value not in self.values:
                return False
        counter = {}
        for card in cards:
            if card.value not in counter:
                counter[card.value] = 0
            counter[card.value] += 1
        if 3 in counter.values():
            return True
        return False

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        cards = self.cards
        for card in cards:
            if card.value not in self.values:
                return False
        counter = {}
        for card in cards:
            if card.value not in counter:
                counter[card.value] = 0
            counter[card.value] += 1
        if 2 in counter.values():
            return True
        return False

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        if len(self.cards) < 5:
            return None
        if self.is_straight_flush():
            return "straight flush"
        if self.is_flush():
            return "flush"
        if self.is_straight():
            return "straight"
        if self.is_full_house():
            return "full house"
        if self.is_four_of_a_kind():
            return "four of a kind"
        if self.is_three_of_a_kind():
            return "three of a kind"
        if self.is_pair():
            return "pair"
        return "high card"

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        hand_type = self.get_hand_type()
        if hand_type is not None:
            return f"I got a {hand_type} with cards: {', '.join(str(card) for card in self.cards)}"
        else:
            return f"I'm holding {', '.join(str(card) for card in self.cards)}"


if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "straight"

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "four of a kind"
