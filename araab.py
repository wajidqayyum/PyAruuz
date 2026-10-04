class Araab:
    # Arabic/Urdu diacritics
    characters = [
        "\u0651", # Shadda
        "\u0650", # Kasra
        "\u0652", # Sukun
        "\u0656", # Subscript Alef
        "\u0658", # Noon Ghunna Mark
        "\u0670", # Superscript Alef
        "\u064B", # Fathatan
        "\u064D", # Kasratan
        "\u064E", # Fatha
        "\u064F", # Damma
        "\u0654"  # Hamza Above
    ]

    @staticmethod
    def remove_tashdid(word):
        if not word: return ""
        res = ""
        for i in range(len(word)):
            if word[i] == Araab.characters[0]: # Shadd
                if i > 0:
                    char = word[i-1]
                    res = res[:-1] + char + Araab.characters[2] + char + Araab.characters[8]
            else:
                res += word[i]
        return res

    @staticmethod
    def remove_araab(word):
        for char in Araab.characters:
            word = word.replace(char, "")
        return word
