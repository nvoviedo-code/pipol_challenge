import os
import json
import logging
import datetime

from ..constants import CACHE_DIR

logger = logging.getLogger("Cache")

class Cache():
    """
    Class that manages the cache for scraped data.
    """
    
    def __init__(self):
        self.__cache_file_name = self.__get_chache_filename()        

    def __get_chache_filename(self):
        """"
        Generates a cache filename based on the URL and current date.
        """
        date = datetime.datetime.now().strftime("%Y%m%d")
        return os.path.join(CACHE_DIR, f"{date}_cache.json")

    def is_available(self):
        """
        Check if the cache file exists and is not empty.
        """
        if os.path.exists(self.__cache_file_name):
            logger.info(f"Cache file {self.__cache_file_name} found.")
            try:
                with open(self.__cache_file_name) as file:
                    data = file.read()
                    return bool(data)
            except Exception as e:
                logger.error(f"Error reading cache file: {e}")
                return False
        else:
            logger.warning(f"Cache file {self.__cache_file_name} not found.")
            return False  
    
    def retrieve_cache_data(self):
        """
        Retrieve data from cache file.
        """
        logger.info(f"Getting cached data from {self.__cache_file_name}")
        try:
            with open(self.__cache_file_name) as file:
                data = file.read()
                logger.info("Cache data loaded successfully.")
                return json.loads(data)
        except Exception as e:
            logger.error(f"Error loading cache data: {e}")
            return []
        
    def save_cache_data(self, data):
        """
        Save the scraped data to the cache file.
        """
        if not os.path.exists(CACHE_DIR):
            logger.warning(f"Cache directory {CACHE_DIR} does not exist. Unable to save data.")
            return
        try:
            with open(self.__cache_file_name, 'w') as file:
                json.dump(data, file)
                logger.info(f"Cache data saved to {self.__cache_file_name}.")
        except Exception as e:
            logger.error(f"Error saving cache data: {e}")
            raise
        else:
            logger.info("Cache data saved successfully.")
