"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# ----------------------
# TWIP Agency schemas
# ----------------------

class Lead(BaseModel):
    """
    Marketing/contact leads for TWIP
    Collection name: "lead"
    """
    name: str = Field(..., min_length=2, description="Contact name")
    email: EmailStr = Field(..., description="Contact email")
    business_name: Optional[str] = Field(None, description="Business name")
    message: str = Field(..., min_length=5, description="Message or project details")

# Legacy example from previous demo (kept for reference)
class Inquiry(BaseModel):
    """
    Customer inquiries for custom silver jewelry
    Collection name: "inquiry"
    """
    name: str = Field(..., min_length=2, description="Customer name")
    email: EmailStr = Field(..., description="Customer email")
    phone: Optional[str] = Field(None, description="Optional phone number")
    message: str = Field(..., min_length=10, description="Inquiry details or design ideas")
    budget: Optional[str] = Field(None, description="Approximate budget or range")
    reference_link: Optional[str] = Field(None, description="Link to inspiration or reference image")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
