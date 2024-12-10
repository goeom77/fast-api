from fastapi import FastAPI, Query
from pydantic import BaseModel
from packaging.version import Version

app = FastAPI()

class VersionResponse(BaseModel):
    status: int
    code: str
    message: str
    data: dict

@app.get("/api/v1/app-version", response_model=VersionResponse)
async def get_app_version(
  version: str = Query(..., description="The version of the app")
  ):
    # 기준 버전 정의
    required_version = Version("2.3.4")
    # 입력된 버전 문자열을 Version 객체로 변환
    input_version = Version(version)

    # 버전 비교: 입력된 버전이 기준 버전보다 크거나 같은 경우 업데이트가 필요
    is_update_required = input_version >= required_version

    return {
        "status": 200,
        "code": "S001",
        "message": "Operation successful",
        "data": {
            "isVersionUpdateRequired": is_update_required
        }
    }

# 개발 서버 실행 명령
# uvicorn main:app --reload
