"""Board games."""

class Statistics:
    def __init__(self, filename):
        """Initialize the board games."""
        self.board_games = []
        self.read_file_and_store(filename)

    def read_file_and_store(self, filename):
        """Read the file and store the board games."""
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        if len(parts) == 4:
                            game_name = parts[0].strip()
                            player_names = [x.strip() for x in parts[1].split(',')]
                            result_type = parts[2].strip()
                            results = [x.strip() for x in parts[3].split(',')]
                            
                            board_game = {
                                'game_name': game_name,
                                'player_names': player_names,
                                'result_type': result_type,
                                'results': results
                            }
                            self.board_games.append(board_game)
        except FileNotFoundError:
            pass

    def get_player_names(self):
        """Sinu 'players' funktsioon."""
        players = set()
        for game in self.board_games:
            players.update(game['player_names'])
        return list(players)

    def get_game_names(self):
        """Sinu 'game_list' funktsioon."""
        names = set()
        for game in self.board_games:
            names.add(game['game_name'])
        return list(names)

    def get_games_played_amount(self):
        """Sinu 'total_game_played' funktsioon."""
        return len(self.board_games)

    def get_game_results(self, game_name):
        """Sinu 'get_game_results' - parandatud .lower() osaga."""
        for game in self.board_games:
            if game['game_name'].strip().lower() == game_name.strip().lower():
                return game['result_type'], game['results'], game['player_names']
        return None, None, None

    def winners_by_game(self, game_name):
        """Sinu 'winners_by_game' - koos väikese parandusega Chessi jaoks."""
        result_type, results, player_names = self.get_game_results(game_name)
        
        if result_type is None:
            return []

        if result_type == 'points':
            int_results = [int(r) for r in results]
            max_points = max(int_results)
            return [player_names[i] for i, res in enumerate(int_results) if res == max_points]

        elif result_type.lower() in ['win', 'winner']:
            winners = [player_names[i] for i, res in enumerate(results) 
                      if res.lower() == 'win' or res in player_names]
            return winners if winners else [r for r in results if r in player_names]

        elif result_type == 'places':
            if results[0].isdigit():
                int_results = [int(r) for r in results]
                min_place = min(int_results)
                return [player_names[i] for i, res in enumerate(int_results) if res == min_place]
            else:
                return [results[0]]
        return []

    def most_wins(self):
        """Player with the most wins."""
        win_counts = {}
        for game in self.board_games:
            winners = self.winners_by_game(game['game_name'])
            for winner in winners:
                win_counts[winner] = win_counts.get(winner, 0) + 1
        if not win_counts:
            return []
        max_wins = max(win_counts.values())
        return [player for player, count in win_counts.items() if count == max_wins]

    def most_losses(self):
        """Player with the most losses."""
        loss_counts = {}
        for game in self.board_games:
            result_type, results, player_names = self.get_game_results(game['game_name'])
            if result_type is None:
                continue
            if result_type == 'points':
                int_results = [int(r) for r in results]
                min_points = min(int_results)
                losers = [player_names[i] for i, res in enumerate(int_results) if res == min_points]
                for loser in losers:
                    loss_counts[loser] = loss_counts.get(loser, 0) + 1
            elif result_type.lower() in ['win', 'winner']:
                losers = [player_names[i] for i, res in enumerate(results) 
                          if res.lower() != 'win' and res not in player_names]
                for loser in losers:
                    loss_counts[loser] = loss_counts.get(loser, 0) + 1
            elif result_type == 'places':
                if results[0].isdigit():
                    int_results = [int(r) for r in results]
                    max_place = max(int_results)
                    losers = [player_names[i] for i, res in enumerate(int_results) if res == max_place]
                    for loser in losers:
                        loss_counts[loser] = loss_counts.get(loser, 0) + 1
                else:
                    losers = [results[-1]]
                    for loser in losers:
                        loss_counts[loser] = loss_counts.get(loser, 0) + 1
        if not loss_counts:
            return []
        max_losses = max(loss_counts.values())
        return [player for player, count in loss_counts.items() if count == max_losses]

    def most_frequent_winner(self):
        """Player with the most wins across all games."""
        win_counts = {}
        for game in self.board_games:
            winners = self.winners_by_game(game['game_name'])
            for winner in winners:
                win_counts[winner] = win_counts.get(winner, 0) + 1
        if not win_counts:
            return []
        max_wins = max(win_counts.values())
        return [player for player, count in win_counts.items() if count == max_wins]

    def most_frequent_loser(self):
        """Player with the most losses across all games."""
        loss_counts = {}
        for game in self.board_games:
            result_type, results, player_names = self.get_game_results(game['game_name'])
            if result_type is None:
                continue
            if result_type == 'points':
                int_results = [int(r) for r in results]
                min_points = min(int_results)
                losers = [player_names[i] for i, res in enumerate(int_results) if res == min_points]
                for loser in losers:
                    loss_counts[loser] = loss_counts.get(loser, 0) + 1
            elif result_type.lower() in ['win', 'winner']:
                losers = [player_names[i] for i, res in enumerate(results) 
                          if res.lower() != 'win' and res not in player_names]
                for loser in losers:
                    loss_counts[loser] = loss_counts.get(loser, 0) + 1
            elif result_type == 'places':
                if results[0].isdigit():
                    int_results = [int(r) for r in results]
                    max_place = max(int_results)
                    losers = [player_names[i] for i, res in enumerate(int_results) if res == max_place]
                    for loser in losers:
                        loss_counts[loser] = loss_counts.get(loser, 0) + 1
                else:
                    losers = [results[-1]]
                    for loser in losers:
                        loss_counts[loser] = loss_counts.get(loser, 0) + 1
        if not loss_counts:
            return []
        max_losses = max(loss_counts.values())
        return [player for player, count in loss_counts.items() if count == max_losses]

    def record_holders(self):
        """Record holders for wins and losses."""
        return {
            'most_wins': self.most_frequent_winner(),
            'most_losses': self.most_frequent_loser()
        }







file_location = r'C:\Users\siim.heinsaar\Desktop\CODESSS\OOP\BoardGames_task\file.txt'
Statistics = Statistics(file_location)
Statistics.read_file_and_store(file_location)
#print(Statistics.get_Statistics())
#print(Statistics.players())
#print(Statistics.game_list())
#print(Statistics.total_game_played())
#print(Statistics.results_by_player('ekke'))
#print(Statistics.get_game_results('Chess'))
#print(Statistics.winners_by_game('game of thrones'))
print(Statistics.most_wins())
print(Statistics.most_losses())
print(Statistics.most_frequent_winner())
print(Statistics.most_frequent_loser())
print(Statistics.record_holders())