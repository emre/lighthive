import asyncio
import uuid
from collections import OrderedDict
import time

import httpx


async def rpc_request(client, node, call, params):
    response = await client.post(
        node,
        json={
            "jsonrpc": "2.0",
            "method": call,
            "params": params,
            "id": str(uuid.uuid4())
        }
    )

    if response.status_code != 200:
        raise Exception("Invalid status code!")

    response_json = response.json()

    # sanity check
    head_block_number = response_json.get("result", {}).get("head_block_number")
    if not head_block_number:
        raise Exception("Malformed response!")

    if 'error' in response_json:
        raise Exception(response.get("error"))

    return response


async def compare_nodes(nodes, logger):
    start_time = time.time()
    node_performance_results = {}

    for node in nodes:
        async with httpx.AsyncClient() as client:
            try:
                response = await rpc_request(
                    client, node, "database_api.get_dynamic_global_properties",
                    {})
                measured_time_in_seconds = response.elapsed.total_seconds()
            except Exception as e:
                logger.error(e)
                measured_time_in_seconds = -1

            node_performance_results[node] = measured_time_in_seconds

    node_performance_results_sorted = OrderedDict(sorted(node_performance_results.items(), key=lambda x: x[1]))
    measurements_in_str = ""
    for node, time_elapsed in node_performance_results_sorted.items():
        measurements_in_str += f"{node}: {time_elapsed:.2f} [s]\n"
    logger.info("Measurements: \n%s", measurements_in_str)
    total_time_elapsed = time.time() - start_time
    logger.info(f"Automatic node selection took  {total_time_elapsed:.2f} seconds.")
    return list(node_performance_results_sorted.keys())


def sort_nodes_by_response_time(nodes, logger):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(compare_nodes(nodes, logger))