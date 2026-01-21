import asyncpg
import asyncio


class DbUtils:
    def __init__(self, **args):
        self.user_name = args.get("username")
        self.password = args.get("password")
        self.db_name = args.get("db_name")
        self.host = args.get("host")
        self.port = int(args.get("port", 5432))  # Convert port to int
        self.pool = None
        self.query=args.get("query")

    async def init_pool(self):
        try:
            if self.pool is None:
                # MUST await the pool creation
                self.pool = await asyncpg.create_pool(
                    user=self.user_name,
                    password=self.password,
                    database=self.db_name,
                    host=self.host,
                    port=self.port,
                    max_size=5,
                    min_size=2
                )
                print("--- Pool initialized successfully ---")

            # Use a connection from the pool to test it
            async with self.pool.acquire() as conn:
                if str(self.query).startswith("select"):
                    ss=await conn.fetch(self.query)
                    return [dict(j) for j in ss]
                else:
                    ss=await conn.execute(self.query)


        except Exception as e:
            print(f"Connection Error: {e}")


# --- How to run async code ---
async def main():
    db = DbUtils(username="postgres",
                 password="admin",
                 db_name="postgres",
                 host="localhost",
                 port="5432",
                 query="select * from public.sample_data")
    print(await db.init_pool())


if __name__ == "__main__":
    asyncio.run(main())