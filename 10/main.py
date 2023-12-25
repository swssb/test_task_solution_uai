import gspread
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

GITHUB_API_URL = "https://api.github.com/users/"

gc = gspread.service_account(filename='github-api-storage-9922562ba17b.json')


async def parse_github_user(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(GITHUB_API_URL + username)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="GitHub API request failed")


@app.get("/github/{username}")
async def get_github_user_and_save_to_gsheet(username: str):
    try:
        github_user = await parse_github_user(username)
        sh = gc.open('github')
        worksheet = sh.sheet1
        data = worksheet.get_all_records()
        if not data:
            keys = list(github_user.keys())
            worksheet.append_row(keys)
        next_row_values = list(github_user.values())

        worksheet.append_row(next_row_values)
        return JSONResponse(content={"success": "ok"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


@app.get("/gsheet/")
async def get_data_from_sheet():
    try:
        sh = gc.open('github')
        worksheet = sh.sheet1
        all_data = worksheet.get_all_values()
        if not all_data:
            return JSONResponse(content={"error": "No data in Google Sheet"})
        keys = all_data[0]
        values = all_data[1:]
        data = [dict(zip(keys, row)) for row in values]
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)})
