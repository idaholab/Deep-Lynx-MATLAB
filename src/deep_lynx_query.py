# Copyright 2023, Battelle Energy Alliance, LLC

import os
import settings
import pandas as pd
import deep_lynx
import logging
import time
import src
import pandas as pd


def query_deep_lynx(file_id: str):
    """
    Retrieve data from Deep Lynx
    Args
        file_id (string): the id of a file stored in Deep Lynx
    """
    # Get deep lynx environment variables
    api_client = src.api_client
    container_id = os.environ["CONTAINER_ID"]
    data_source_id = os.environ["DATA_SOURCE_ID"]

    # Retrieve file from Deep Lynx
    data_sources_api = deep_lynx.DataSourcesApi(api_client)
    dl_file_path = retrieve_file(data_sources_api, file_id)

    # Write csv to local repository
    query_df = pd.read_csv(dl_file_path)



def retrieve_file(data_sources_api: deep_lynx.DataSourcesApi, file_id: str):
    """
    Retrieve a file from Deep Lynx
    Args
        data_sources_api (deep_lynx.DataSourcesApi): deep lynx data source api
        file_id (string): the id of a file
        container_id (str): deep lynx container id
    """
    # Get deep lynx environment variables
    api_client = src.api_client
    container_id = os.environ["CONTAINER_ID"]
    data_source_id = os.environ["DATA_SOURCE_ID"]

    retrieve_file = data_sources_api.retrieve_file(container_id, file_id)

    if not retrieve_file.is_error:
        retrieve_file = retrieve_file.to_dict()["value"]
        path = retrieve_file["adapter_file_path"] + retrieve_file["file_name"]
        return path

