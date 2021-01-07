class CharacterCounter:
    """ Joins the equal methods but with different realisation"""

    @staticmethod
    def count_character_with_loop(string: str) -> str:
        """ Returns character number in given string with loop usage

        Examples:
            >>> CharacterCounter.count_character_with_loop('1234')
            '4'
            >>> CharacterCounter.count_character_with_loop('abcdefghijklmnoprstuvwxyz')
            '25'
        """
        counter = 0
        for char in string:
            counter += 1
        return str(counter)

    @staticmethod
    def count_character_build_in(string: str) -> str:
        """ Returns character number in given string with biult-in method

        Examples:
            >>> CharacterCounter.count_character_build_in('1234')
            '4'
            >>> CharacterCounter.count_character_build_in('abcdefghijklmnoprstuvwxyz')
            '25'
        """
        return str(len(string))
