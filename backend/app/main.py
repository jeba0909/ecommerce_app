# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.config import get_settings

# Routers
from app.routers import auth, products, orders

settings = get_settings()

app = FastAPI(title="Ecommerce RBAC API")

# --------------------
# CORS SETUP
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# INCLUDE ROUTERS
# --------------------
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])


# --------------------
# STARTUP EVENT
# --------------------
@app.on_event("startup")
def on_startup():
    init_db()


# --------------------
# ROOT ENDPOINT
# --------------------
@app.get("/")
def root():
    return {"message": "Ecommerce API Running!"}
