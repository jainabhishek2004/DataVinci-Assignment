from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Abhishek%402004@localhost:5432/myappdb")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    impressions = Column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)


class CampaignBase(BaseModel):
    name: str
    status: str
    clicks: int
    cost: float
    impressions: int

class CampaignResponse(CampaignBase):
    id: int

    class Config:
        from_attributes = True


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/campaigns", response_model=List[CampaignResponse])
def get_campaigns(status: str = None):
    db = next(get_db())
    try:
        query = db.query(Campaign)
        if status:
            query = query.filter(Campaign.status == status)
        campaigns = query.all()
        return campaigns
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 