import asyncio
from http import HTTPStatus
from fastapi import FastAPI
from api.schemas import Result
from httpx import Client, AsyncClient, RequestError

app = FastAPI(docs_url=None, redoc_url=None)


# We simulate a list of 100 URLs to perform the queries
urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 100


@app.get("/task_sync", status_code=HTTPStatus.OK, response_model=Result)
async def task_sync() -> Result:
    """
    Synchronously performs HTTP requests to the provided URLs.

    This endpoint uses synchronous requests to perform 100 HTTP calls to the specified URLs.
    It waits for each response before proceeding to the next request, which may result in longer
    execution times compared to the asynchronous version.

    Returns:
        Result: A JSON response containing a success message and the total number of requests made.
    Raises:
        Exception: If an error occurs during the HTTP requests.
    """
    try:
        with Client(timeout=None) as client:
            results = [client.get(url).json() for url in urls]

        return Result(
            success={
                "message": "Sync requests completed",
                "results_count": len(results),
            }
        )

    except Exception as e:
        return Result(erro=f"(get_response_sync) --> {e}")


@app.get("/task_async", status_code=HTTPStatus.OK, response_model=Result)
async def async_requests() -> Result:
    """
    Asynchronously performs HTTP requests to the provided URLs.

    This endpoint uses asynchronous programming to perform 100 HTTP requests concurrently.
    It gathers the results of all requests and filters out any unsuccessful ones.
    This improves execution time compared to the synchronous version by handling multiple
    requests simultaneously.

    Returns:
        Result: A JSON response containing a success message and the total number of successful requests made.

    Raises:
        Exception: If an error occurs during the execution of HTTP requests.
    """
    try:
        async with AsyncClient(timeout=None) as async_client:
            tasks = [fetch_data(async_client, url) for url in urls]
            results = await asyncio.gather(*tasks)
            results = [result for result in results if result.success]
        return Result(
            success={
                "message": "Async requests completed",
                "results_count": len(results),
            }
        )

    except Exception as e:
        return Result(erro=f"(get_response_sync) --> {e}")


async def fetch_data(client: AsyncClient, url: str) -> Result:
    """
    Fetches data asynchronously from a given URL.

    This function performs a single asynchronous HTTP request to the specified URL using
    the provided `AsyncClient`. It awaits the response and returns the result in the form
    of a `Result` object. If the request fails, it returns a `Result` with an error message.

    Args:
        client (AsyncClient): The asynchronous HTTP client used to perform the request.
        url (str): The URL to send the HTTP request to.

    Returns:
        Result: A `Result` object containing the successful JSON response or an error message.

    Raises:
        httpx.RequestError: If an error occurs while making the HTTP request.
    """
    try:
        response = await client.get(url)
        return Result(success=response.json())
    except RequestError as e:
        return Result(erro=f"(fetch_data) -> {e}")
