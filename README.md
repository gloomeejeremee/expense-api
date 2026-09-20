# 클라우드컴퓨팅실습 — 3주차 과제

FastAPI 백엔드(가계부 지출 관리 API)를 Render에 배포하고, 이를 호출하는 프론트엔드를 Vercel에 배포한 연동 실습입니다.

## 배포 주소

- **GitHub 저장소**: (이 저장소 주소)
- **Vercel 배포 페이지**: (여기에 Vercel 주소 입력)
- **백엔드 Swagger UI**: (여기에 https://your-app.onrender.com/docs 입력)

## 프로젝트 구성

```
.
├── index.html          # 개인 소개 페이지
├── api-demo.html        # 프론트엔드–백엔드 연동 실습 페이지
└── expense-api/          # FastAPI 백엔드
    ├── app/
    │   ├── main.py             # 앱 생성 + 라우터 조립 + CORS 설정
    │   ├── models.py           # Pydantic 요청/응답 모델
    │   └── routers/
    │       └── transactions.py # 거래 CRUD 엔드포인트
    ├── requirements.txt
    └── .gitignore
```

## 주요 기능

- `GET /` , `GET /health` — 기본 상태 확인
- `POST /transactions` — 거래 등록 (Pydantic 검증: 금액 0 초과, 카테고리 1~50자 등)
- `GET /transactions` — 거래 목록 조회
- `GET /transactions/{id}` — 단건 조회 (없으면 404)
- `DELETE /transactions/{id}` — 삭제 (없으면 404)

`api-demo.html`에서 위 엔드포인트를 실제로 호출해 등록·조회·삭제를 테스트할 수 있습니다.

## 사용한 기술

- Backend: FastAPI, Pydantic, Uvicorn → **Render** 배포
- Frontend: 순수 HTML/CSS/JS (fetch API) → **Vercel** 배포
- Version control: GitHub

## 실습 기록

### ① 결과 확인
(여기에 /docs 에서 등록→조회→삭제→404 확인 캡처 붙이기)

### ② 핵심 개념 되새김
- CRUD 네 동작과 HTTP 메서드 대응: (한 줄로 정리)
- Pydantic 검증이 막아주는 것: (한 줄로 정리)
- /docs 자동 문서가 어디서 나오는가: (한 줄로 정리)

### ③ 자유 로그
(오늘 배운 것, 막힌 곳과 해결 과정, AI 활용 내용을 자유롭게 기록)
