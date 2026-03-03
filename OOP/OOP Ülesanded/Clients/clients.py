"""Client."""
from typing import Optional
import csv

class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        result = (self.current_amount - self.starting_amount) / self.account_age
        return result


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients = []
    with open(filename, "r") as f:
        for line in f:
            # Eeldame, et fail on kujul: nimi,pank,vanus,algsumma,lõppsumma
            parts = line.strip().split(",")
            if len(parts) == 5:
                # Loome uue Client objekti
                client = Client(parts[0], parts[1], int(parts[2]), int(parts[3]), int(parts[4]))
                clients.append(client)
    return clients


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    all_clients = read_from_file_into_list(filename)
    
    filtered_clients = []
    for client in all_clients:
        if client.bank == bank:
            filtered_clients.append(client)
            
    return filtered_clients

def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    clients = read_from_file_into_list(filename)
    best_client = None
    max_earnings = 0

    for client in clients:
        earnings = client.earnings_per_day()
        if earnings > 0:
            if best_client is None or earnings > max_earnings:
                max_earnings = earnings
                best_client = client
            elif earnings == max_earnings:
                # Kui teenistus on sama, vali lühema ajaga klient
                if client.account_age < best_client.account_age:
                    best_client = client
    
    return best_client


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    clients = read_from_file_into_list(filename)
    worst_client = None
    min_earnings = 0

    for client in clients:
        earnings = client.earnings_per_day()
        if earnings < 0:
            if worst_client is None or earnings < min_earnings:
                min_earnings = earnings
                worst_client = client
            elif earnings == min_earnings:
                # Kui kaotus on sama, vali lühema ajaga klient
                if client.account_age < worst_client.account_age:
                    worst_client = client
                    
    return worst_client


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
