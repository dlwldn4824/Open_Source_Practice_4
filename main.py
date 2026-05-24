from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

JSON_UTF8 = "application/json; charset=utf-8"


@app.middleware("http")
async def set_json_charset(request, call_next):
    response = await call_next(request)
    content_type = response.headers.get("content-type", "")
    if content_type.startswith("application/json") and "charset=" not in content_type:
        response.headers["content-type"] = JSON_UTF8
    return response

DATA_FILE = Path("courses.json")


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


def load_courses():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_courses(courses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)


@app.get("/")
def root():
    return {"message": "FastAPI Course Records Server"}


@app.get("/courses")
def get_courses():
    courses = load_courses()
    return JSONResponse(content=courses, media_type=JSON_UTF8)


@app.post("/courses")
def add_course(course: Course):
    courses = load_courses()
    new_course = course.model_dump() if hasattr(course, "model_dump") else course.dict()
    courses.append(new_course)
    save_courses(courses)

    return JSONResponse(
        content={
            "message": "수강기록이 추가되었습니다.",
            "added_course": new_course,
        },
        media_type=JSON_UTF8,
    )
