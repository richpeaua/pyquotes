import random

def find_quote_file_pos(quotes_file_path):
    """Finds the start and end offsets of a quote inside quote file

    Args:
        quote_file_path (str): full file path to quote file
    Returns:
        dict: A dictionary with the start and end offsets of each quote in quote file 
    """

    quote_file_map = {}

    # The entire "with" block below reads the quote file, finds the index number of the FIRST found quote-end marker (% symbol), adds that index+1 (+1 because the beginning 
    # of next quote is AFTER the end marker) to "start_marker_pos" variable, updates the "f.seek()" to start next read from that new start position, adds an entry to the "quote_file_map" 
    # dict with the start position and the end position of current quote and then repeats until end of file.
    with open(quotes_file_path) as f:
        start_marker_pos = 0
        quote_number = 0
        end = False
        while not end:
            f.seek(start_marker_pos)
            file = f.read()
            if file:
                quote_file_map[quote_number] = {'start': start_marker_pos, 'end': 0}
                start_marker_pos += file.index('%')+1
                quote_file_map[quote_number]['end'] = start_marker_pos-1
                quote_number += 1
            else:
                end = True

    return quote_file_map

def return_rand_quote(quotes_map, quotes_file_path):
    """Returns random quote from quotes file within the start and end offsets in quote_map dict

    Args:
        quote_map (dict): Dictionary containing the start and end offsets of each quote in the quote file
        quote_file_path (str): full file path to quote file
    Returns:
        str: A single quote from quotes file
    """

    rand_quote_idx = random.randint(0, len(quotes_map) - 1)

    with open(quotes_file_path) as f:
        f.seek(quotes_map[rand_quote_idx]['start'])
        quote = f.read(quotes_map[rand_quote_idx]['end'] - quotes_map[rand_quote_idx]['start'])
    
    return quote.strip()


if __name__ == "__main__":
    import time

    QUOTES_FILE = "./quotes.txt"
    QUOTES_MAP = find_quote_file_pos(QUOTES_FILE)

    while True:
        print(return_rand_quote(QUOTES_MAP, QUOTES_FILE) + "\n")
        time.sleep(2)

