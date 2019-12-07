"""
Checks whether we can call the hello endpoint.
"""

import pytest

import pressure_sensor.__main__ as main


@pytest.fixture
async def app(app):
    app.router.add_routes(main.routes)
    return app


async def test_hello(app, client):
    res = await client.post('/volume')
    assert res.status == 200
    assert res.content_type == 'application/json'
