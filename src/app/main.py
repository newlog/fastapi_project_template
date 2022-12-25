from fastapi import FastAPI

from config.fastapi import settings as fastapi_settings
from config.logging import settings as logging_settings
from routers import configure_routes

logging_settings.configure_logging()

app = FastAPI(title='Instagram Follower Tracker')
fastapi_settings.cors_setup(app)
configure_routes(app)


@app.get('/')
async def root():
    return 'Go to /api/v1/followers/{$account} to get the followers of a given $account'


# Only needed to debug
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
