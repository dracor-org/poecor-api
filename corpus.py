class Corpus:
    """Corpus of poems

    Attributes:
        name (str): Name of the corpus. To be used as an ID.
        title (str): Title of the corpus.
        description (str): Description of the corpus.
        metrics (dict): Metrics of the corpus.

    Example:
        A response of the API should look like:

        {
        'name': 'postdata',
        'title': 'POSTDATA Corpus',
        'description': 'POSTDATA Knowledge Graph of Poetry. See https://postdata.linhd.uned.es',
        'metrics':
            {
            'authors': 1192,
            'poems': 10071,
            'stanzas': 81122,
            'verses': 544498,
            'words': 2988230,
            'grammatical_syllables': 2116388,
            'metrical_syllables': 1259036}}
    """
    # Corpus Name
    name = None

    # Title of the Corpus
    title = None

    # Description of the Corpus
    description = None

    # corpus metrics
    metrics = None