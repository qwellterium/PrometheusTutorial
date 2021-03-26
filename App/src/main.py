from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import Route

from starlette_exporter import PrometheusMiddleware, handle_metrics


middlewares = [Middleware(PrometheusMiddleware, prefix="app")]


async def main(request):
    return JSONResponse({"hello": "world"}, status_code=200)


routes = [Route("/", main, methods=["GET", "POST"]), Route("/metrics", handle_metrics)]


App = Starlette(routes=routes, middleware=middlewares)
