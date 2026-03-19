from fastapi import APIRouter
from app.database import collection
from app.models import Expense

router = APIRouter()

@router.post("/expense")
def add_expense(expense: Expense):
    data = expense.dict()
    data["status"] = "pending"
    collection.insert_one(data)
    return {"message": "added"}

@router.get("/expenses")
def get_expenses():
    return list(collection.find({}, {"_id": 0}))

@router.get("/summary")
def summary():
    expenses = list(collection.find({}, {"_id": 0}))
    total = sum(item["amount"] for item in expenses)
    return {"total": total}
