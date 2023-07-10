# Copyright 2023, Battelle Energy Alliance, LLC

from importlib.metadata import metadata
import os
import logging
import deep_lynx
import utils
import json
import datetime
import time
import src


def import_to_deep_lynx(import_file: str, event: dict = None):
    """
    Import data into Deep Lynx
    Args
        import_file (string): the file path to import into Deep Lynx
        event (dictionary): a dictionary of the event information
    """
    # Get deep lynx environment variables
    api_client = src.api_client
    container_id = os.environ["CONTAINER_ID"]
    data_source_id = os.environ["DATA_SOURCE_ID"]

    done = False
    did_succeed = False
    start = time.time()
    path = os.path.join(os.getcwd() + '/' + import_file)
    while not done:
        # Check if import file exists
        if os.path.exists(path):
            logging.info(f'Found {import_file}.')
            # Import data into Deep Lynx
            data_sources_api = deep_lynx.DataSourcesApi(api_client)
            info = upload_file(data_sources_api, import_file)
            logging.info('Success: Run complete. Output data sent.')

            if event:
                # Send event signaling complete
                event['status'] = 'complete'
                event['modifiedDate'] = datetime.datetime.now().isoformat()
                #data_sources_api.create_manual_import(event, container_id, data_source_id)
                logging.info('Event sent.')
            done = True
            did_succeed = True
            break
        else:
            logging.info(
                f'Fail: {import_file} not found. Trying again in {os.getenv("IMPORT_FILE_WAIT_SECONDS")} seconds')
            end = time.time()
            # Break out of infinite loop
            if end - start > float(os.getenv("IMPORT_FILE_WAIT_SECONDS")) * 20:
                logging.info(f'Fail: In the final attempt, {import_file} was not found.')
                done = True
                break
            # Sleep for wait seconds
            else:
                logging.info(
                    f'Fail: {import_file} was not found. Trying again in {os.getenv("IMPORT_FILE_WAIT_SECONDS")} seconds'
                )
                time.sleep(int(os.getenv("IMPORT_FILE_WAIT_SECONDS")))
    if did_succeed:
        return True
    return False


def upload_file(data_sources_api: deep_lynx.DataSourcesApi, file_path: str):
    """
    Uploads a file into Deep Lynx   
    Args
        data_sources_api (deep_lynx.DataSourcesApi): deep lynx data source api
        file_path (string): the file path to import into Deep Lynx
    """
    # Get deep lynx environment variables
    api_client = src.api_client
    container_id = os.environ["CONTAINER_ID"]
    data_source_id = os.environ["DATA_SOURCE_ID"]

    file_return = data_sources_api.upload_file(container_id,
                                               data_source_id,
                                               file=file_path,
                                               metadata=os.getenv("METADATA"),
                                               async_req=False)
    print(file_return)
    if len(file_return["value"]) > 0:
        logging.info("Successfully imported data to deep lynx")
        print("Successfully imported data to deep lynx")
    else:
        logging.error("Could not import data into Deep Lynx. Check log file for more information")
        print("Could not import data into Deep Lynx. Check log file for more information")
    return file_return
