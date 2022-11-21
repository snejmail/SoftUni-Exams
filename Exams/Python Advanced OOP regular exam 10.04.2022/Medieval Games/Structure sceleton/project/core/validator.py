class Validator:
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_negative(number, message):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_below_12(number, message):
        if number < 12:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_not_in_range(number, min_range, max_range, message):
        if number < min_range or number > max_range:
            raise ValueError(message)

    @staticmethod
    def check_players_stamina_for_duel(player1, player2):
        check_players_stam_res = ''
        if player1.stamina > 0 and player2.stamina > 0:
            return None
        for pl in [player1, player2]:
            if pl.stamina == 0:
                check_players_stam_res += f'Player {pl.name} does not have enough stamina.\n'
        return check_players_stam_res.strip()
