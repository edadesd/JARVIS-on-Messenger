'''
The GetConfig class abstracts retrieving a key or data file name from the
config file. Create a GetConfig using the name of the key as an argument.
It will attempt to retrieve the key file with that name and save it as a string
to the object's result data member. If retrieving the key raises an exception,
result will be set to False, so it is recommended to check the value of the
variable after creating a GetConfig object.

Usage:
accessor = util.GetConfig("NAME_OF_KEY_OR_DATA_FILE")
key_string = accessor.result
assert(key_string)

Return:
key_string is either a string representing the string associated with
NAME_OF_KEY_OR_DATA_FILE in config.py, or False.
'''

class GetConfig:

    def __init__(self, line_name):
        import os
        import config

        # When a new line is added to config.py it needs to be added
        # here as well.
        config_lines = {

            # Facebook (+ Wit)
            'ACCESS_TOKEN': config.ACCESS_TOKEN,
            'VERIFY_TOKEN': config.VERIFY_TOKEN,
            'WIT_AI_ACCESS_TOKEN': config.WIT_AI_ACCESS_TOKEN,

            # Offline data sources
            'FACTS_SOURCE_FILE': config.FACTS_SOURCE_FILE,
            'JOKES_SOURCE_FILE': config.JOKES_SOURCE_FILE,
            'QUOTES_SOURCE_FILE': config.QUOTES_SOURCE_FILE,

            # Access token files
            'SPOTIFY_TOKEN_FILE': config.SPOTIFY_TOKEN_FILE,

            # API Keys
            'GOODREADS_ACCESS_TOKEN': config.GOODREADS_ACCESS_TOKEN,
            'GOOGLE_URL_SHORTENER_API_KEY':
                config.GOOGLE_URL_SHORTENER_API_KEY,
            'MAPQUEST_CONSUMER_KEY': config.MAPQUEST_CONSUMER_KEY,
            'MUSIXMATCH_API_KEY': config.MUSIXMATCH_API_KEY,
            'NEWS_API_KEY': config.NEWS_API_KEY,
            'OPEN_WEATHER_MAP_ACCESS_TOKEN':
                config.OPEN_WEATHER_MAP_ACCESS_TOKEN,
            'SPOTIFY_API_KEY': config.SPOTIFY_API_KEY,
            'TIME_ZONE_DB_API_KEY': config.TIME_ZONE_DB_API_KEY,
            'TMDB_API_KEY': config.TMDB_API_KEY,
            'WORDS_API_KEY': config.WORDS_API_KEY,
            'YOUTUBE_DATA_API_KEY': config.YOUTUBE_DATA_API_KEY
        }

        try:
            self.result = os.environ.get(line_name, config_lines[line_name])
        except:
            self.result = False