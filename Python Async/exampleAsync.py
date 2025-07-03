import asyncio

async def api_call():
    print("Calling API...")
    await asyncio.sleep(2)
    print("API done")
    return "api_result"

async def db_query():
    print("Querying DB...")
    await asyncio.sleep(2)
    print("DB done")
    return "db_result"

async def log_message():
    print("Logging...")
    await asyncio.sleep(1)
    print("Logged")

async def main():
    # Run API call and DB query in parallel
    result_api, result_db = await asyncio.gather(
        api_call(),
        db_query()
    )

    # After both are done, log the message
    await log_message()

    print(f"Results: {result_api}, {result_db}")

asyncio.run(main())
