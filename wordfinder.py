"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["hello", "hey", "how"]
    True

    >>> wf.random() in ["hello", "hey", "how"]
    True

    >>> wf.random() in ["hello", "hey", "how""]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["potato", "tomato", "kale","mango","apple","grapes"]
    True

    >>> swf.random() in ["potato", "tomato", "kale","mango","apple","grapes"]
    True

    >>> swf.random() in ["potato", "tomato", "kale","mango","apple","grapes"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
