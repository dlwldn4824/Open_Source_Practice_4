from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

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
    return courses


@app.post("/courses")
def add_course(course: Course):
    courses = load_courses()
    courses.append(course.dict())
    save_courses(courses)

    return {
        "message": "수강기록이 추가되었습니다.",
        "added_course": course
    }
