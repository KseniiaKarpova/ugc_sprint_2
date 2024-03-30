import pytest
import uuid
from functional.settings import test_settings
import random


@pytest.mark.parametrize(
    'in_data, out_data',
    [
        (
                {
                    "film_id": str(uuid.uuid4()),
                },
                {'status_code': 201},
        ),
        (
                {
                    "film_id": str(uuid.uuid4()),
                },
                {'status_code': 201},
        ),
        (
                {
                    "film_id": str('asdasdasdsadsa'),
                },
                {'status_code': 404},
        ),
    ]
)
@pytest.mark.asyncio
async def test_like(make_post_request, get_access_token ,in_data, out_data):
    access_token = await get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    body, status = await make_post_request(endpoint="/api/v1/reviews", service_url=test_settings.reviews_service_url, json={
        'film_id': uuid.uuid4()}, headers=headers)
    review_id = body['_id']
    body, status = await make_post_request(endpoint="/api/v1/review_like/{}", service_url=test_settings.reviews_service_url, json=in_data, headers=headers)
    assert status == out_data['status_code']


@pytest.mark.parametrize(
    'in_data, out_data',
    [
        (
                {
                    "film_id": str(uuid.uuid4()),
                },
                {'status_code': 201},
        ),
        (
                {
                    "film_id": str(uuid.uuid4()),
                },
                {'status_code': 201},
        ),
        (
                {
                    "film_id": str('asdasdasdsadsa'),
                },
                {'status_code': 404},
        ),
    ]
)
@pytest.mark.asyncio
async def test_dislike(make_post_request, get_access_token ,in_data, out_data):
    access_token = await get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    body, status = await make_post_request(endpoint="/api/v1/reviews/film/dislike", service_url=test_settings.reviews_service_url, json=in_data, headers=headers)
    assert status == out_data['status_code']


@pytest.mark.parametrize(
    'in_data, out_data',
    [
        (
                {
                    "film_id": str(uuid.uuid4()),
                    "text": "Some text",
                    "mark": random.randint(0, 10),
                },
                {'status_code': 201},
        ),
        (
                {
                    "film_id": str(uuid.uuid4()),
                    "text": "Some text",
                    "mark": random.randint(0, 10),
                },
                {'status_code': 201},
        ),
        (
                {
                    "film_id": str('asdasdasdsadsa'),
                    "text": "Some text",
                    "mark": random.randint(11, 100),
                },
                {'status_code': 404},
        ),
        (
                {
                    "film_id": uuid.uuid4(),
                    "text": "Some text",
                    "mark": random.randint(11, 100),
                },
                {'status_code': 404},
        ),
    ]
)
@pytest.mark.asyncio
async def test_review_creation(make_post_request, get_access_token ,in_data, out_data):
    access_token = await get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    body, status = await make_post_request(endpoint="/api/v1/reviews", service_url=test_settings.reviews_service_url, json=in_data, headers=headers)
    assert status == out_data['status_code']
