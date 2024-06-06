# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
phone_book = {}
for _ in range(n):
    name, number = input().strip().split()
    phone_book[name] = number

queries = []
try:
    while True:
        query = input().strip()
        queries.append(query)
except EOFError:
    pass

for query in queries:
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")