# BDOK CRUD test

Clone project and install requirements from requirements.txt \
Use Postman or Insomnia to send rerequests


Run server: python main.py 

Create new product [POST]: http://0.0.0.0:8000/product/ \
Retrieve all products [GET]: http://0.0.0.0:8000/product/ \
Retrieve a single product [GET]: http://0.0.0.0:8000/product/{id} \
Updating the product data [PUT]: http://0.0.0.0:8000/product/{id} \
Delete product [DELETE]: http://0.0.0.0:8000/product/{id}



Example for add product:\
{\
    "name": "Samsung Galaxy s22",\
    "price": "1500",\
    "description": "good phone"\
}

<img src="https://gcdnb.pbrd.co/images/a0vr2GfrCMvt.png?o=1">
