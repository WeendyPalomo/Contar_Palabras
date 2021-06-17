#https://parzibyte.me/blog

archivo = open('Starwars.txt',encoding='utf')
libro=archivo.read()
force = libro.count("force")
luke = libro.count("Luke")
ben = libro.count("Ben")
want = libro.count("want")
archivo.close()

print("force", force)
print("Luke", luke)
print("want", want)
print("Ben", ben)