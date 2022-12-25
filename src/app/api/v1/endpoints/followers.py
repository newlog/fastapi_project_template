from fastapi import APIRouter
import logging


from app.dependencies.instagram import InstagramClient

router = APIRouter()


@router.get("/{account}", tags=["followers"])
async def account_followers(account: str):
    insta_client = InstagramClient()
    insta_client.authenticate()
    followers = insta_client.get_followers(account)
    logging.info(followers)


# TODO
# 1. Configure Celery to execute 1) accounts to follow & posts to like 2) posts to unlike & accounts to unfollow
# 2. Write Celery task to check tracked accounts, store accounts to follow
# 3. Write Celery tasks to read accounts to follow & like random posts & store in mongo accounts followed & posts liked
# 4. Write Celery task to read posts to unlike & accounts to unfollow
