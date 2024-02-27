# Lightspeed X Series Python Wrapper (lightspeed_x)

This is a simple Python wrapper for the Lightspeed X Series API. It allows you to easily interact with your Lightspeed POS system using Python code.

> **PLEASE NOTE:** This package is intended for my portfolio, rather than public use. It is subject to change or abandonment. Feel free to use it, at your own risk.

## Installation

Install the package using pip:

```Bash
pip install lightspeed_x
```

## Usage

```python
from lightspeed_x import LightspeedX


# Replace with your credentials
personal_token = "YOUR_PERSONAL_TOKEN"
domain_prefix = "YOUR_DOMAIN_PREFIX"

# Create a LightspeedX object
lightspeed = LightspeedX(personal_token, domain_prefix)

# Get all products
products = lightspeed.get("/products")

# Create a new product
new_product = {
"name": "T-Shirt",
"sku": "TSHIRT123",
"price": 19.99,
}

lightspeed.post("/products", data=new_product)

# Update a product. You must specify api_version 2.1 to use this endpoint.
product_id = 456
updated_product = {
"name": "T-Shirt (Updated)",
"price": 24.99,
}

lightspeed.put(
    f"/products/{product_id}",
    data=updated_product,
    api_version="2.1",
)

# Delete a product
lightspeed.delete(f"/products/{product_id}")
```

## Features

- Supports all available Lightspeed X Series API endpoints.
- Provides convenient methods for GET, POST, PUT, and DELETE requests.
- Automatically handles authentication and request formatting.
- Allows specifying the API version for each request. **Default:** `2.0`

## Documentation

Full API reference: https://x-series-api.lightspeedhq.com/reference

## Contributing

Pull requests and suggestions are welcome! Please see the CONTRIBUTING.md file for details.

## License

MIT License

## Additional Notes

Refer to the Lightspeed X Series API documentation for more details on available endpoints and data structures.

Remember to replace the placeholder credentials with your own before using the code.
