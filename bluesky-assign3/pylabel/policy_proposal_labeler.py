import re, json, time, csv
from urllib.parse import urlparse
from datetime import datetime, timezone
from pathlib import Path
from typing import List

import pandas as pd
from atproto import Client

class PolicyLabeler:
    def __init__(self, client: Client, input_dir):
        self.client = client
   
    def moderate_post(self, url: str) -> List[str]:
        """
        Apply moderation to the post specified by the given url
        """
        return []