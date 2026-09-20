from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import transactions

app = FastAPI(title="지출 관리 API")

# 프론트엔드(Vercel)와 백엔드(Render)가 서로 다른 주소이므로
# 브라우저의 CORS 정책을 통과하려면 이 설정이 필요합니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "지출 관리 API에 오신 것을 환영합니다"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(transactions.router)
