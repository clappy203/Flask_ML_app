import json
import numpy as np
import pandas as pd


def process_input(request_data: str) -> np.array:
    '''
    Creates a processing function to transform inputs to expected outcome
    '''
    parsed_body = json.loads(request_data)["inputs"]
    assert len(parsed_body.items()) == 13, "'inputs' must have 13 features"

    return pd.DataFrame(parsed_body)
