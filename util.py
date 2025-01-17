"""Core functionality. Maybe this module is obsolete and more of a util"""
import hashlib


# Stuff to move somewhere else follows below

# TODO: This is already a method of the SparqlQuery class. Can be removed later, but keep for reference now.
def inject(
        query: str,
        uris: list,
        placeholder: str = "$") -> str:
    """Inject URIs into a SPARQL query containing placeholders.

    This helper function takes a query and a list of uris and replaces each occurrence of a designated pattern,
    {placeholder}{position in uris}, e.g. $1 with the first URI in the supplied list of uris,
    $2 with the second.
    It expects, that the parts to be replaced are already enclosed in angle brackets, e.g. <$1>. The placeholder
    prefix can be specified, default is "$".

    Args:
        query (str): SPARQL query containing one or more placeholders to be replaced with URIs.
        uris (list): List of URIs to be injected into the query.
        placeholder (str, optional): prefix of the placeholder. Defaults to "$".

    Example:
        >>> print(inject("SELECT * WHERE {<$1> <$2> <$3> .}", ["http://first.uri", "http://second.uri", "http://third.uri"])
        SELECT * WHERE {<http://first.uri> <http://second.uri> <http://third.uri> .}

    Returns:
        str: Query with injected uris.
    """
    # loop over uris and replace the placeholder with an uri at position n
    n = 1
    for uri in uris:
        to_replace = placeholder + str(n)
        query = query.replace(to_replace, uri)
        n = n + 1

    return query


def shorthash(textstring: str, chars: int = 8) -> str:
    """Create a trunctaded md5 hash of a string

    Args:
        textstring: Text to produce a shorthash from.
        chars (int): length of shorted hash. Defaults to 8.

    Returns:
        str: shorted md5hash
    """
    hashed = hashlib.sha1(textstring.encode("UTF-8")).hexdigest()
    shorthash = hashed[:chars]
    return shorthash

