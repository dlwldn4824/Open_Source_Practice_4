# Open_Source_Practice_4

FastAPI 기반 수강 기록 API 서버입니다. `courses.json` 파일에 수강 과목을 저장·조회합니다.

## 요구 사항

- Python 3.10+

## 설치 및 실행

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

서버 기본 주소: `http://127.0.0.1:8000`

API 문서(Swagger UI): `http://127.0.0.1:8000/docs`

## API

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/` | 서버 상태 확인 |
| GET | `/courses` | 전체 수강 기록 조회 |
| POST | `/courses` | 수강 기록 추가 |

### POST `/courses` 요청 예시

```json
{
  "course_name": "자료구조",
  "year": "2025",
  "semester": "2",
  "grade": "A+"
}
```

## 프로젝트 구조

```
├── main.py           # FastAPI 애플리케이션
├── courses.json      # 수강 기록 데이터
├── requirements.txt
└── .gitignore
```
