"""Board games API."""
from collections import Counter


class Session:
    """Describe a single board game session."""

    def __init__(self, game_name, players, result_type, results):
        """Initialize the session."""
        self.game_name = game_name
        self.players = players
        self.result_type = result_type.strip().lower()
        self.results = results
        self.winners = []
        self.losers = []
        self._calculate_outcomes()

    def _calculate_outcomes(self):
        """Calculate winners and losers based on the result type."""
        if self.result_type == 'points':
            points = [int(p) for p in self.results]
            max_p = max(points)
            min_p = min(points)
            self.winners = [self.players[i] for i, p in enumerate(points) if p == max_p]
            self.losers = [self.players[i] for i, p in enumerate(points) if p == min_p]
        elif self.result_type == 'places':
            self.winners = [self.results[0]]
            self.losers = [self.results[-1]]
        elif self.result_type == 'winner':
            self.winners = [self.results[0]]
            self.losers = [p for p in self.players if p not in self.winners]


class Player:
    """Describe a player."""

    def __init__(self, name):
        """Initialize the player with default stats."""
        self.name = name
        self.plays = 0
        self.wins = 0
        self.played_games = []

    def record_session(self, game_name, is_winner):
        """Record a played session for the player."""
        self.plays += 1
        if is_winner:
            self.wins += 1
        self.played_games.append(game_name)

    def get_favourite_game(self):
        """Return the name of the most frequently played game."""
        if not self.played_games:
            return None
        return Counter(self.played_games).most_common(1)[0][0]


class Game:
    """Describe a specific board game and its statistics."""

    def __init__(self, name):
        """Initialize the game with empty sessions and stats."""
        self.name = name
        self.sessions = []
        self.player_stats = {}

    @property
    def plays(self):
        """Return the total number of sessions played."""
        return len(self.sessions)

    def add_session(self, session: Session):
        """Add a session and update player statistics."""
        self.sessions.append(session)
        for p in session.players:
            if p not in self.player_stats:
                self.player_stats[p] = {'plays': 0, 'wins': 0, 'losses': 0}

            self.player_stats[p]['plays'] += 1
            if p in session.winners:
                self.player_stats[p]['wins'] += 1
            if p in session.losers:
                self.player_stats[p]['losses'] += 1

    def get_most_common_player_amount(self):
        """Return the most common number of players in this game."""
        if not self.sessions:
            return 0
        counts = [len(s.players) for s in self.sessions]
        return Counter(counts).most_common(1)[0][0]

    def get_most_wins(self):
        """Return the player string with the most wins."""
        if not self.player_stats:
            return None
        return max(self.player_stats.keys(), key=lambda k: self.player_stats[k]['wins'])

    def get_most_frequent_winner(self):
        """Return the player string with the highest win ratio."""
        if not self.player_stats:
            return None
        return max(
            self.player_stats.keys(), 
            key=lambda k: self.player_stats[k]['wins'] / self.player_stats[k]['plays']
        )

    def get_most_losses(self):
        """Return the player string with the most losses."""
        if not self.player_stats:
            return None
        return max(self.player_stats.keys(), key=lambda k: self.player_stats[k]['losses'])

    def get_most_frequent_loser(self):
        """Return the player string with the highest loss ratio."""
        if not self.player_stats:
            return None
        return max(
            self.player_stats.keys(), 
            key=lambda k: self.player_stats[k]['losses'] / self.player_stats[k]['plays']
        )

    def get_record_holder(self):
        """Return the player string who holds the highest point record."""
        record_score = -float('inf')
        holder = None
        for s in self.sessions:
            if s.result_type == 'points':
                points = [int(p) for p in s.results]
                for i, score in enumerate(points):
                    if score > record_score:
                        record_score = score
                        holder = s.players[i]
        return holder


class Statistics:
    """Main API class for board game statistics."""

    def __init__(self, filename):
        """Initialize the API and load data from the file."""
        self.players = {}
        self.games = {}
        self.sessions = []
        self._load_data(filename)

    def _load_data(self, filename):
        """Read file and populate internal data structures."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split(';')
                    if len(parts) != 4:
                        continue

                    g_name = parts[0].strip()
                    p_names = [p.strip() for p in parts[1].split(',')]
                    r_type = parts[2].strip()
                    results = [r.strip() for r in parts[3].split(',')]

                    session = Session(g_name, p_names, r_type, results)
                    self.sessions.append(session)

                    if g_name not in self.games:
                        self.games[g_name] = Game(g_name)
                    self.games[g_name].add_session(session)

                    for p in p_names:
                        if p not in self.players:
                            self.players[p] = Player(p)
                        self.players[p].record_session(g_name, p in session.winners)
        except FileNotFoundError:
            pass

    def get(self, path: str):
        """Route the API request to the correct handler."""
        parts = [x for x in path.strip().strip('/').split('/') if x]
        if not parts:
            return "Invalid Path"

        category = parts[0]
        if category in ("players", "games", "total"):
            return self._handle_total(parts)
        if category == "player" and len(parts) == 3:
            return self._handle_player(parts[1], parts[2])
        if category == "game" and len(parts) == 3:
            return self._handle_game(parts[1], parts[2])

        return "Invalid Path"

    def _handle_total(self, parts):
        """Process total, games and players queries."""
        category = parts[0]
        if category == "players":
            return list(self.players.keys())
        if category == "games":
            return list(self.games.keys())

        if len(parts) == 1:
            return len(self.sessions)

        result_type = parts[1].lower()
        return sum(1 for s in self.sessions if s.result_type == result_type)

    def _handle_player(self, name, action):
        """Process queries related to a specific player."""
        if name not in self.players:
            if action in ("amount", "won"):
                return 0
            return None

        player = self.players[name]
        if action == "amount":
            return player.plays
        if action == "favourite":
            return player.get_favourite_game()
        if action == "won":
            return player.wins
            
        return "Invalid Path"

    def _handle_game(self, name, action):
        """Process queries related to a specific game."""
        if name not in self.games:
            if action in ("amount", "player-amount"):
                return 0
            return None

        game = self.games[name]
        actions = {
            "amount": game.plays,
            "player-amount": game.get_most_common_player_amount(),
            "most-wins": game.get_most_wins(),
            "most-frequent-winner": game.get_most_frequent_winner(),
            "most-losses": game.get_most_losses(),
            "most-frequent-loser": game.get_most_frequent_loser(),
            "record-holder": game.get_record_holder()
        }
        return actions.get(action, "Invalid Path")