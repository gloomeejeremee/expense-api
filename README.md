# 클라우드컴퓨팅실습 — 3주차 과제

FastAPI 백엔드(가계부 지출 관리 API)를 Render에 배포하고, 이를 호출하는 프론트엔드를 Vercel에 배포한 연동 실습입니다.

## 배포 주소

- **GitHub 저장소**: (https://github.com/gloomeejeremee/expense-api)
- **Vercel 배포 페이지**: (https://expense-j57mfby72-crocodilelady.vercel.app)
- **백엔드 Swagger UI**: (https://expense-api-55gy.onrender.com/docs)

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
<img width="1381" height="615" alt="스크린샷 2026-09-20 오후 1 36 17" src="https://github.com/user-attachments/assets/62ee0d7c-1e21-4cf8-98a1-8e809e1ffac6" />
<img width="1403" height="634" alt="스크린샷 2026-09-20 오후 1 38 45" src="https://github.com/user-attachments/assets/e0e7ba5e-3e35-44e1-b467-96616d9faa3e" />
<img width="1404" height="617" alt="스크린샷 2026-09-20 오후 1 39 59" src="https://github.com/user-attachments/assets/43ba49c3-88dd-491c-a512-505429d6673f" />
<img width="1397" height="726" alt="스크린샷 2026-09-20 오후 1 40 56" src="https://github.com/user-attachments/assets/263c662b-bb5f-4b39-b9f0-c56c33fc9889" />
<img width="1417" height="578" alt="스크린샷 2026-09-20 오후 1 45 41" src="https://github.com/user-attachments/assets/873d1280-9dd8-4978-96b4-c6d7ef96466d" />
<img width="1377" height="522" alt="스크린샷 2026-09-20 오후 1 46 13" src="https://github.com/user-attachments/assets/341ff734-2472-4c44-b395-eade0464ee2f" />

### ② 핵심 개념 되새김
- CRUD 네 동작과 HTTP 메서드 대응: (한 줄로 정리)
- Pydantic 검증이 막아주는 것: (한 줄로 정리)
- /docs 자동 문서가 어디서 나오는가: (한 줄로 정리)

### ③ 자유 로그
FastAPI로 CRUD API를 만들고 Render에 배포하는 과정을 실습했다. 가장 오래 걸린 부분은 배포 단계였다 —
GitHub에 폴더를 드래그 앤 드롭으로 올릴 때 빈 파일(__init__.py)이 조용히 빠지거나, 폴더 구조 자체가 
평평하게 풀려버리는 문제를 겪었다. 이 때문에 "ModuleNotFoundError: No module named 'app'" 오류로 
배포가 계속 실패했고, GitHub 웹 화면에서 파일명에 경로를 직접 적어 넣는 방식으로 폴더 구조를 복구해서 
해결했다.
프론트엔드(Vercel)와 백엔드(Render)가 서로 다른 도메인이라 CORS 설정이 필요하다는 것도 이번에 알게 됐다.
Claude에게 백엔드 코드 작성, 배포 문제 트러블슈팅(로그 해석), 프론트엔드 연동 페이지 제작을 맡겼고,
로컬에서 실제로 서버를 띄워 각 엔드포인트를 curl로 직접 테스트해 응답이 워크북과 일치하는지 확인했다.
