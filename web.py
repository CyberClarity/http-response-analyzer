import requests

url = input("Enter a Url: ")

if not url.startswith("http"):
    url = "https://" + url

try:
	r = requests.get(url)

	print("\nStatus Code:")
	print(r.status_code)

	print("\nHeaders:")
	print(r.headers)

	print("\nCookies:")
	print(r.cookies)

	print("\nUrl:")
	print(r.url)

	print("\nEncoding:")
	print(r.encoding)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
