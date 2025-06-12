from app import app, db, Product

products = [
    {"name": "Bluetooth Headphones", "category": "Electronics", "price": 99.99, "description": "Wireless headphones with noise cancellation."},
    {"name": "Smartphone", "category": "Electronics", "price": 499.99, "description": "Latest Android smartphone with AMOLED display."},
    {"name": "Laptop", "category": "Electronics", "price": 899.99, "description": "High-performance laptop for work and gaming."},
    {"name": "Cotton T-Shirt", "category": "Apparel", "price": 19.99, "description": "Soft and breathable cotton t-shirt."},
    {"name": "Blue Jeans", "category": "Apparel", "price": 39.99, "description": "Comfortable and stylish jeans."},
    {"name": "Sci-Fi Novel", "category": "Books", "price": 12.99, "description": "Bestselling science fiction story."},
    {"name": "Cookbook", "category": "Books", "price": 15.99, "description": "Healthy and easy recipes for everyday meals."},
    {"name": "Sneakers", "category": "Footwear", "price": 59.99, "description": "Comfortable running shoes."},
    {"name": "Smart Watch", "category": "Electronics", "price": 149.99, "description": "Tracks fitness and notifications."},
    {"name": "Backpack", "category": "Accessories", "price": 29.99, "description": "Durable and spacious travel backpack."}
]

with app.app_context():
    # Create tables
    db.create_all()
    
    # Clear existing data (optional)
    Product.query.delete()

    # Insert products
    for p in products:
        product = Product(
            name=p["name"],
            category=p["category"],
            price=p["price"],
            description=p["description"]
        )
        db.session.add(product)

    db.session.commit()
    print("✅ Products loaded into the database.")

