# mysite
My first real project

I have no experience in making READMEs, so I will just try to describe the destination of this django application:
1) You are able to parse specialized json data into sqlite database as a model "production"
  If you want to do this, type "python manage.py add_data" in your powershell setted(established?) on the project dir 
  (in my case http://www.unisport.dk/api/sample/, but you can set enother similar by settig it as 'products_url' in           mysite\products\management\commands\add_data.py)
2) You are able to create new production model by yourself on http://localhost:8000/products/creation/
3) You can view this models ordered by increasing price and add search query like setting maximum price 
  or typing text, which might be in the name of production
  
Like this..
