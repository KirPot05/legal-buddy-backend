from pydantic import BaseModel


class SummaryResponse(BaseModel):
    summary_english: str
    summary_kannada: str
