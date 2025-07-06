from fastapi import FastAPI, HTTPException, Depends
from service import ProductService
from models.product_model import Product 
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List


app = FastAPI()
engine = create_engine("postgresql+psycopg2://admin:admin@10.194.32.165:5434/postgres")
Session = sessionmaker(bind=engine)
session = Session()