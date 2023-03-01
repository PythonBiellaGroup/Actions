from typing import Any
from fastapi import FastAPI, responses
from starlette.middleware.cors import CORSMiddleware

from app.src.config import settings

app = FastAPI(
    title=f"{settings.PROJECT_NAME}",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
def start_screen() -> Any:
    """Startup route."""
    url_swagger = f"http://{settings.API_ENDPOINT_HOST}:{settings.API_ENDPOINT_PORT}/docs"
    url_redoc = f"http://{settings.API_ENDPOINT_HOST}:{settings.API_ENDPOINT_PORT}/redoc"
    body = (
        "<html><body style='padding: 10px;'><h1>Welcome to PBG Backend:"
        " for the software engineering night</p><p>This version it's working for:"
        f"</p><ul><li><a href={url_swagger}>Link to the Swagger"
        f" documentation</a></li><li><a href={url_redoc}>Link to the Redoc documentation</a></li></ul></body></html>"
    )
    return responses.HTMLResponse(content=body)
