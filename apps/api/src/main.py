from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.documents import router as documents_router
from src.api.v1.chat import router as chat_router

app = FastAPI(
    title="AI Research Assistant API",
    description="API for AI Research Assistant application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include API routers
app.include_router(documents_router)
app.include_router(chat_router)

# CORS configuration to allow frontend communication
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Research Assistant API"}

@app.get("/debug/routes")
def list_routes():
    routes = []
    for route in app.routes:
        if hasattr(route, 'path'):
            routes.append({
                'path': route.path,
                'methods': route.methods if hasattr(route, 'methods') else [],
            })
    return {'routes': routes}

@app.options("/{path:path}")
async def options_handler(path: str):
    return {"message": "OK"}
