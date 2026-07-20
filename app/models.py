from pydantic import BaseModel


class Recommendation(BaseModel):
    channel: str
    product: str
    current_spend: float
    sales: float
    roi: float
    recommended_spend: float
    action: str